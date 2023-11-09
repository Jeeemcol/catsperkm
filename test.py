"""
Check CSV how long longest catsperkm string is
to test against the results from precision which
don't look quite right
"""
import pandas as pd

def calc_decimal(string):
    """Returns the decimal portion from string number or 0"""
    if "." in string:
        decimal = string.split(".")[1]
        return len(decimal)
    return "0"

# Read the CSV file into a DataFrame, forcing strings
df = pd.read_csv('APHA0384-Cats_Per_Km.csv', dtype=str)
# `result` is a Series: a one-dimensional labeled array indexed by int
# This is a pandas specific structure. This is returned by map()
total_length_result = df['CatsPerKm'].map(len)
# Series functions:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html6666
largest_value = total_length_result.max()
index_of_largest = total_length_result.idxmax()
element_with_max_length = df['CatsPerKm'][index_of_largest]
print(element_with_max_length)

scale_result = df['CatsPerKm'].map(calc_decimal)
print(type(scale_result))
#largest_scale_value = scale_result.max() <<< throws error here
#index_of_largest_scale = scale_result.idxmax()
#scale_element_with_max_length = df['CatsPerKm'][index_of_largest_scale]
#print(f"Largest decimal length: {largest_scale_value}")
def get_scale():
    return scale_result
