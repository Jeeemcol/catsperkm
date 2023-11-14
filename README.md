# Cats per km (UK)
This project uses Python and Mariadb to extract, transform and load data from the UK Government about cat population per km in the UK.
## Install

Install requirements from `requirements.txt`
```
$ pip install -r requirements.txt
```
## Run
### Into database
If you want to load the transformed data into a database, run `csv_to_sql_import.py`
```
$ python csv_to_sql_import.py
```
### CSV based analysis
#### Generate a top 10
This will open a matplotlib plot
```
>>> import analyse_csv
>>> analyse_csv.print_top_10()
```

# Notes on data

* "1,152.02"
* 544.7151399
* 9.94E-05

Are all present in the CatsPerKm column
  
  
# Data 
Cats per square kilometre

Published by: Animal and Plant Health Agency Last updated: 01 November 2023 Topic: Not added Licence: Open Government Licence

  

Summary

This dataset is a modelled dataset, describing the mean number of cats per square kilometre across GB. The figures are aligned to the British national grid, with a population estimate provided for each 1km square. These data were generated as part of the delivery of commissioned research. The data contained within this dataset are modelled figures, based on national estimates for pet population, and available information on Veterinary activity across GB. The data are accurate as of 01/01/2015. The data provided are summarised to the 1km level. Further information on this research is available in a research publication by James Aegerter, David Fouracre & Graham C. Smith, discussing the structure and density of pet cat and dog populations across Great Britain. Attribution statement: ©Crown Copyright, APHA 2016

  

https://www.data.gov.uk/dataset/9d475e06-3885-4a90-b8c0-77fea13f92e6/cats-per-square-kilometre

http://data.defra.gov.uk/Agriculture/APHA0384-Cats_Per_Km.csv

  
# @todo

* pypi OS grid converting 
https://pypi.org/project/OSGridConverter/
* map OS points onto a map of the UK

## [License](https://github.com/Jeeemcol/get-email-adestra-piano-integration/blob/main/README.md#license)

This code is provided under the MIT License. See the  [LICENSE](https://github.com/Jeeemcol/get-email-adestra-piano-integration/blob/main/LICENSE)  file for details.

## Author

-   Jeeemcol