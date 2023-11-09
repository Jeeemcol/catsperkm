"""
Calculates the precision and scale of CatsPerKm
Based on sternb0t/precision_and_scale_of_csv.ipynb gist:
https://gist.github.com/sternb0t/791e5c7e5064c3f6a7f7835e2d163dd3
CSV Data: http://data.defra.gov.uk/Agriculture/APHA0384-Cats_Per_Km.csv
"""
from decimal import Decimal
import pandas as pd

# Read the CSV file into a DataFrame, forcing strings
df = pd.read_csv('APHA0384-Cats_Per_Km.csv', dtype=str)

def calc_precision():
    """
    Calculates the precision of the cats per km column for SQL decimal.
    df (dataframe) is the structure, not an object, etc. It has specific
    location parameters defined that we're selecting (the 'CatsPerKm'
    column and the second row (starts at 0) and then applying map() to it.
    For each column it runs a lambda function which calculates the length
    element-wise after . is replaced with nothing (so the dot is taken out).
    Then the resulting DataFrame (which doesn't persist beyond this line)
    is checked with the max function. At which point whichever length is max is
    returned. We then have our value for precision we need to specify in the 
    db.
    """
    precision = df['CatsPerKm'][1:].map(lambda x: len(
        str(x).replace('.', ''))).max()
    return precision

def calc_scale():
    """
    Calculates the scale of the cats per km column for SQL decimal.
    """
    scale = df['CatsPerKm'][1:].map(lambda x: len(
        str(x).rsplit('.', maxsplit=1)[-1])).max()
    return scale
