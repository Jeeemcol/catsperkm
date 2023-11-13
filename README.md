notes on data:
"1,152.02"
544.7151399
9.94E-05
all present in the CatsPerKm column


```
import pandas as pd

data = {
    'column one': ['abc', 'def', 'ghi', 'jkl'],
    'column two': ['5,363.22', '0.456', '7.89E-05', '1000']
}

df1 = df2 = pd.DataFrame(data)

df1['column two'] = df1['column two'].replace(',', '', regex=True).astype(float)
df2['column two'] = pd.to_numeric(df2['column two'], errors='coerce')

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

```

2 methods: both accomplish the handling of commas


mariadb python cats per square kilometre in the UK

pip install csvkit
pip install mysql-connector-python
pip install pandas

in mariadb:
CREATE DATABASE catspersqkm;
USE catspersqkm;
CREATE TABLE mytable (
    OS1kmRef varchar,
    CatsPerKm decimal(6,2)
);


Cats per square kilometre
Published by: Animal and Plant Health Agency Last updated: 01 November 2023 Topic: Not added Licence: Open Government Licence

Summary
This dataset is a modelled dataset, describing the mean number of cats per square kilometre across GB. The figures are aligned to the British national grid, with a population estimate provided for each 1km square. These data were generated as part of the delivery of commissioned research. The data contained within this dataset are modelled figures, based on national estimates for pet population, and available information on Veterinary activity across GB. The data are accurate as of 01/01/2015. The data provided are summarised to the 1km level. Further information on this research is available in a research publication by James Aegerter, David Fouracre & Graham C. Smith, discussing the structure and density of pet cat and dog populations across Great Britain. Attribution statement: ©Crown Copyright, APHA 2016

https://www.data.gov.uk/dataset/9d475e06-3885-4a90-b8c0-77fea13f92e6/cats-per-square-kilometre
    http://data.defra.gov.uk/Agriculture/APHA0384-Cats_Per_Km.csv

    * pypi OS grid converting

    https://pypi.org/project/OSGridConverter/

    * csv into mariadb guide

    https://raghavendar-d.medium.com/import-csv-files-into-mariadb-43a87536f6e5
    
    apt install python3-pip

    pip3 install csvkit

    pip3 install mysql-connector-python