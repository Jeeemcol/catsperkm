"""
Analyses the source cat CSV file and generates a report in matplotlib
"""
import matplotlib.pyplot as plt
from cats_csv import df

def print_top_10():
    subset_df = df.iloc[:10]
    subset_df.plot(kind='bar', x='OS1kmRef', y='CatsPerKm', legend=False)
    plt.title('Number of Cats per Kilometer')
    plt.xlabel('Ordnance Survey Grid Reference')
    plt.ylabel('Cats per Kilometer')
    plt.show()
