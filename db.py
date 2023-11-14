"""
Manages database functions
Adapted from:
dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
"""
import logging
import time
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE

class DB:
    """
    This DB class lets you connect to Mariadb;
    create db for cats per km; upload the csv;
    """

    def __init__(self, decimal_precision, decimal_scale):
        self.decimal_precision = decimal_precision
        self.decimal_scale = decimal_scale
        self.connection = None
        # Set up logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Log to console
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Also log to a file
        file_handler = logging.FileHandler("cpy-errors.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _connect(self):
        attempts = 3
        delay = 2
        attempt = 1

        if self.connection is None:
            # Implement a reconnection routine
            while attempt <= attempts:
                try:
                    self.connection = mysql.connector.connect(
                        host=DB_HOST,
                        user=DB_USER,
                        password=DB_PASSWORD
                    )
                    self.logger.info("Connected successfully")
                    return True
                except mysql.connector.Error as err:
                    self.logger.error("Connection failed: %s", err)
                    self.connection = None
                # Progressive reconnect delay
                time.sleep(delay ** attempt)
                attempt += 1

        return False

    def _disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            self.logger.info("Connection closed")

        return self.connection

    def _create_database(self):
        if self.connection is not None:
            # Create a cursor to execute SQL statements
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_DATABASE}"
            try:
                cur = self.connection.cursor()
                cur.execute(create_db_query)
                self.logger.info("Database created")
            except mysql.connector.Error as err:
                self.logger.error("Create db failed: %s", err)

    def _create_table(self):
        """
        Create the CREATE TABLE statement with dynamic precision
        and dynamic scale for the decimal, as a multi line f-string
        """
        create_table_sql = (
            f"CREATE TABLE IF NOT EXISTS `cats_per_km` ("
            f"  `OS1kmRef` varchar(255) NOT NULL,"
            f"  `CatsPerKm` decimal({self.decimal_precision}, "
            f"{self.decimal_scale}) NOT NULL,"
            f"  PRIMARY KEY (`OS1kmRef`)"
            f") ENGINE=InnoDB;"
        )

        try:
            cur = self.connection.cursor()
            cur.execute(f"USE {DB_DATABASE}")
            cur.execute(create_table_sql)
            self.logger.info("Table created")
        except mysql.connector.Error as err:
            self.logger.error("Create table failed: %s", err)

    def setup(self):
        """This connects to Mariadb and creates the db and table"""
        self._connect()
        self._create_database()
        self._create_table()
        return self.connection

    def closedown(self):
        """This shuts down the db object including Mariadb connection"""
        return self._disconnect()
