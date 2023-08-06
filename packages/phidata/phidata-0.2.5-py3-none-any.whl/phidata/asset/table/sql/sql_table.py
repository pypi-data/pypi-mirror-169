from typing import Optional, Any, Union, List, Dict, Tuple
from typing_extensions import Literal

from sqlalchemy.engine import Engine, Connection
from sqlalchemy.exc import ResourceClosedError

from phidata.asset import DataAsset, DataAssetArgs
from phidata.utils.enums import ExtendedEnum
from phidata.utils.log import logger


class SqlType(ExtendedEnum):
    POSTGRES = "POSTGRES"


class SqlTableArgs(DataAssetArgs):
    # Table Name
    name: str
    # Type of SQL table
    sql_type: SqlType
    # Table schema
    db_schema: Optional[str] = None
    # airflow connection_id can be used for running workflows remotely
    db_conn_id: Optional[str] = None
    # a db_conn_url can be used to create the sqlalchemy.engine.Engine object
    db_conn_url: Optional[str] = None
    # sqlalchemy.engine.(Engine or Connection)
    # Using SQLAlchemy makes it possible to use any DB supported by that library.
    # NOTE: db_engine is required but can be derived using
    # db_conn_url when running locally and
    # db_conn_id when running remotely
    db_engine: Optional[Union[Engine, Connection]] = None


class SqlTable(DataAsset):
    """Base Class for Sql tables"""

    def __init__(
        self,
        name: Optional[str] = None,
        sql_type: Optional[SqlType] = None,
        db_schema: Optional[str] = None,
        db_conn_id: Optional[str] = None,
        db_conn_url: Optional[str] = None,
        db_engine: Optional[Union[Engine, Connection]] = None,
    ) -> None:
        super().__init__()
        self.args: Optional[SqlTableArgs] = None
        if name is not None and sql_type is not None:
            try:
                self.args = SqlTableArgs(
                    name=name,
                    sql_type=sql_type,
                    db_schema=db_schema,
                    db_conn_id=db_conn_id,
                    db_conn_url=db_conn_url,
                    db_engine=db_engine,
                )
            except Exception as e:
                logger.error(f"Args for {self.__class__.__name__} are not valid")
                raise

    @property
    def sql_type(self) -> Optional[SqlType]:
        return self.args.sql_type if self.args else None

    @sql_type.setter
    def sql_type(self, sql_type: SqlType) -> None:
        if self.args and sql_type:
            self.args.sql_type = sql_type

    @property
    def db_conn_id(self) -> Optional[str]:
        return self.args.db_conn_id if self.args else None

    @db_conn_id.setter
    def db_conn_id(self, db_conn_id: str) -> None:
        if self.args and db_conn_id:
            self.args.db_conn_id = db_conn_id

    @property
    def db_schema(self) -> Optional[str]:
        return self.args.db_schema if self.args else None

    @db_schema.setter
    def db_schema(self, db_schema: str) -> None:
        if self.args and db_schema:
            self.args.db_schema = db_schema

    @property
    def db_conn_url(self) -> Optional[str]:
        return self.args.db_conn_url if self.args else None

    @db_conn_url.setter
    def db_conn_url(self, db_conn_url: str) -> None:
        if self.args and db_conn_url:
            self.args.db_conn_url = db_conn_url

    @property
    def db_engine(self) -> Optional[Union[Engine, Connection]]:
        return self.args.db_engine if self.args else None

    @db_engine.setter
    def db_engine(self, db_engine: Union[Engine, Connection]) -> None:
        if self.args and db_engine:
            self.args.db_engine = db_engine

    def create_db_engine_using_conn_url(self) -> None:
        # Create the SQLAlchemy engine using db_conn_url

        if self.db_conn_url is None:
            return

        try:
            from sqlalchemy import create_engine

            logger.info(f"Creating db_engine using db_conn_url: {self.db_conn_url}")
            db_engine = create_engine(self.db_conn_url)
            logger.debug(f"db_engine: {db_engine}")
            if isinstance(db_engine, tuple) and len(db_engine) > 0:
                self.db_engine = db_engine[0]
            else:
                self.db_engine = db_engine
        except Exception as e:
            logger.error(f"Error creating db_engine using {self.db_conn_url}")
            logger.error(e)
            return

    def create_db_engine_using_conn_id(self) -> None:
        # Create the SQLAlchemy engine using db_conn_id

        if self.db_conn_id is None:
            return

        try:
            from airflow.providers.postgres.hooks.postgres import PostgresHook

            logger.info(f"Creating db_engine using db_conn_id: {self.db_conn_id}")
            if self.sql_type == SqlType.POSTGRES:
                pg_hook = PostgresHook(postgres_conn_id=self.db_conn_id)
                self.db_engine = pg_hook.get_sqlalchemy_engine()
        except Exception as e:
            logger.error(f"Error creating db_engine using {self.db_conn_id}")
            logger.error(e)
            return

    def create_db_engine(self) -> None:
        if self.db_engine is not None:
            return

        phidata_runtime: Literal["local", "airflow"] = self.phidata_runtime
        if phidata_runtime == "local":
            self.create_db_engine_using_conn_url()
        elif phidata_runtime == "airflow":
            self.create_db_engine_using_conn_id()

    ######################################################
    ## Write table
    ######################################################

    def write_pandas_df(
        self,
        df: Optional[Any] = None,
        # How to behave if the table already exists.
        # fail: Raise a ValueError.
        # replace: Drop the table before inserting new values.
        # append: Insert new values to the existing table.
        if_exists: Optional[Literal["fail", "replace", "append"]] = None,
        # Write DataFrame index as a column.
        # Uses index_label as the column name in the table.
        index: Optional[bool] = None,
        # Column label for index column(s).
        # If None is given (default) and index is True, then the index names are used.
        # A sequence should be given if the DataFrame uses MultiIndex.
        index_label: Optional[Union[str, List[str]]] = None,
        # Specify the number of rows in each batch to be written at a time.
        # By default, all rows will be written at once.
        chunksize: Optional[int] = None,
    ) -> bool:
        """
        Write DataFrame to table.
        """

        # SqlTable not yet initialized
        if self.args is None:
            return False

        # Check name is available
        if self.name is None:
            logger.error("SqlTable name not available")
            return False

        # Check engine is available
        if self.db_engine is None:
            self.create_db_engine()
            if self.db_engine is None:
                logger.error("DbEngine not available")
                return False

        # write to table
        import pandas as pd

        if df is None or not isinstance(df, pd.DataFrame):
            logger.error("DataFrame invalid")
            return False

        rows_in_df = df.shape[0]
        logger.info(f"Writing {rows_in_df} rows to table: {self.name}")

        # create a dict of args provided
        not_null_args: Dict[str, Any] = {}
        if self.db_schema:
            not_null_args["schema"] = self.db_schema
        if if_exists:
            not_null_args["if_exists"] = if_exists
        if index:
            not_null_args["index"] = index
        if index_label:
            not_null_args["index_label"] = index_label
        if chunksize:
            not_null_args["chunksize"] = chunksize

        try:
            with self.db_engine.connect() as connection:
                df.to_sql(
                    name=self.name,
                    con=connection,
                    **not_null_args,
                )
                logger.info(f"--**-- Done")
            return True
        except Exception:
            logger.error("Could not write table: {}".format(self.name))
            raise

    ######################################################
    ## Read table
    ######################################################

    def read_pandas_df(
        self,
        index_col: Optional[Union[str, List[str]]] = None,
        coerce_float: bool = True,
        parse_dates: Optional[Union[List, Dict]] = None,
        columns: Optional[List[str]] = None,
        chunksize: Optional[int] = None,
    ) -> Optional[Any]:
        """
        Read table into a DataFrame.

        Args:
            index_col : str or list of str, optional, default: None
                Column(s) to set as index(MultiIndex).
            coerce_float : bool, default True
                Attempts to convert values of non-string, non-numeric objects (like
                decimal.Decimal) to floating point. Can result in loss of Precision.
            parse_dates : list or dict, default None
                - List of column names to parse as dates.
                - Dict of ``{column_name: format string}`` where format string is
                strftime compatible in case of parsing string times or is one of
                (D, s, ns, ms, us) in case of parsing integer timestamps.
                - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
                to the keyword arguments of :func:`pandas.to_datetime`
                Especially useful with databases without native Datetime support,
                such as SQLite.
            columns : list, default None
                List of column names to select from SQL table.
            chunksize : int, default None
                If specified, returns an iterator where `chunksize` is the number of
                rows to include in each chunk.

        Returns:
            DataFrame or Iterator[DataFrame]
            A SQL table is returned as two-dimensional data structure with labeled
            axes.
        """

        # SqlTable not yet initialized
        if self.args is None:
            return False

        # Check db_engine is available
        if self.db_engine is None:
            self.create_db_engine()
            if self.db_engine is None:
                logger.error("DbEngine not available")
                return False

        # read sql table
        import pandas as pd

        logger.info("Reading table: {}".format(self.name))

        # create a dict of args provided
        not_null_args: Dict[str, Any] = {}
        if self.db_schema:
            not_null_args["schema"] = self.db_schema
        if index_col:
            not_null_args["index_col"] = index_col
        if coerce_float:
            not_null_args["coerce_float"] = coerce_float
        if parse_dates:
            not_null_args["parse_dates"] = parse_dates
        if columns:
            not_null_args["columns"] = columns
        if chunksize:
            not_null_args["chunksize"] = chunksize

        try:
            with self.db_engine.connect() as connection:
                result_df = pd.read_sql_table(
                    table_name=self.name,
                    con=connection,
                    **not_null_args,
                )
            return result_df
        except Exception:
            logger.error(f"Could not read table: {self.name}")
            raise

    def run_sql_query(
        self,
        sql_query: str,
        index_col: Optional[Union[str, List[str]]] = None,
        coerce_float: bool = True,
        parse_dates: Optional[Union[List, Dict]] = None,
        columns: Optional[List[str]] = None,
        chunksize: Optional[int] = None,
    ) -> Optional[Any]:
        """
        Run SQL query using pandas.read_sql()

        Args:
            index_col : str or list of str, optional, default: None
                Column(s) to set as index(MultiIndex).
            coerce_float : bool, default True
                Attempts to convert values of non-string, non-numeric objects (like
                decimal.Decimal) to floating point. Can result in loss of Precision.
            parse_dates : list or dict, default None
                - List of column names to parse as dates.
                - Dict of ``{column_name: format string}`` where format string is
                strftime compatible in case of parsing string times or is one of
                (D, s, ns, ms, us) in case of parsing integer timestamps.
                - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
                to the keyword arguments of :func:`pandas.to_datetime`
                Especially useful with databases without native Datetime support,
                such as SQLite.
            columns : list, default None
                List of column names to select from SQL table.
            chunksize : int, default None
                If specified, returns an iterator where `chunksize` is the number of
                rows to include in each chunk.

        Returns:
            DataFrame or Iterator[DataFrame]
            A SQL table is returned as two-dimensional data structure with labeled
            axes.
        """

        # SqlTable not yet initialized
        if self.args is None:
            return None

        # Check db_engine is available
        if self.db_engine is None:
            self.create_db_engine()
            if self.db_engine is None:
                logger.error("DbEngine not available")
                return None

        # run sql query
        import pandas as pd

        logger.info("Running Query:\n{}".format(sql_query))

        # create a dict of args provided
        not_null_args: Dict[str, Any] = {}
        if self.db_schema:
            not_null_args["schema"] = self.db_schema
        if index_col:
            not_null_args["index_col"] = index_col
        if coerce_float:
            not_null_args["coerce_float"] = coerce_float
        if parse_dates:
            not_null_args["parse_dates"] = parse_dates
        if columns:
            not_null_args["columns"] = columns
        if chunksize:
            not_null_args["chunksize"] = chunksize

        try:
            with self.db_engine.connect() as connection:
                result_df = pd.read_sql(
                    sql=sql_query,
                    con=connection,
                    **not_null_args,
                )
            return result_df
        except ResourceClosedError as rce:
            logger.info(
                f"The result object was closed automatically, returning no rows."
            )
        # except Exception as e:
        #     logger.error(f"Sql query failed: {e}")
        return None

    ######################################################
    ## Drop table
    ######################################################

    def delete(self) -> bool:
        try:
            result = self.run_sql_query(f"DROP TABLE {self.name};")
        except Exception as e:
            logger.error(f"Drop table failed: {e}")
        return True
