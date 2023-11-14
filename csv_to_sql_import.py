"""
Runs the program to process cats per km csv creates database
(mariadb), table and uploads the data.
"""
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import cats_csv
import db
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE

precision = cats_csv.calc_precision()
scale = cats_csv.calc_scale()

Database = db.DB(precision, scale)
connection = Database.setup()
encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}/{DB_DATABASE}"
)

# use sqlalchemy engine to write using the dataframe to_sql method
# col 1 is our primary key so we don't need the dataframe row index
cats_csv.df.to_sql("cats_per_km", engine, if_exists="replace", index=False)
Database.closedown()
