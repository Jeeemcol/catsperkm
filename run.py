"""
Runs the program to analyse cats per km csv creates database
(mariadb), table and uploads the data.
"""
import cats_csv
import db

precision = cats_csv.calc_precision()
scale = cats_csv.calc_scale()
Database = db.DB(precision, scale)
Database.setup()
