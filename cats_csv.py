"""
Calculates the precision and scale of CatsPerKm
CSV Data: http://data.defra.gov.uk/Agriculture/APHA0384-Cats_Per_Km.csv
"""
from decimal import Decimal
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('APHA0384-Cats_Per_Km.csv')
# The CSV contains the following: "0.000102236" "8.24E-05" "5,363.22"
# we need to remove the commas. Scientific notation is fine
df['CatsPerKm'] = df['CatsPerKm'].replace(',', '', regex=True).astype(float)

def calc_precision():
    """
    Calculates the precision of the cats per km column for SQL decimal.
    df (dataframe) is the structure, not an object, etc. It has specific
    location parameters defined that we're selecting (the 'CatsPerKm'
    column and the second row (starts at 0) and then applying map() to
    the result.
    For each column it runs a lambda function which calculates the length
    element-wise after . is replaced with nothing (so the dot is taken out).
    Then the resulting DataFrame (which doesn't persist beyond this line)
    is checked with the max function. At which point whichever length is max 
    is returned. We then have our value for precision we need to specify 
    in the db
    """
    precision = df['CatsPerKm'][1:].map(lambda x:
                                        len(str(x).replace('.', ''))).max()
    return precision

def calc_scale():
    """
    Calculates the scale of the cats per km column for SQL decimal.
    """
    scale = df['CatsPerKm'][1:].map(lambda x: len(
        str(x).rsplit('.', maxsplit=1)[-1])).max()
    return scale
