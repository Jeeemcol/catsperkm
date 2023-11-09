"""
Runs the program to analyse cats per km csv creates database
(mariadb), table and uploads the data.
"""
import cats_csv
import db

print(cats_csv.calc_precision())
print(cats_csv.calc_scale())
#db.setup(cats_csv.calc_precision())
#db.set_precision(precision)
