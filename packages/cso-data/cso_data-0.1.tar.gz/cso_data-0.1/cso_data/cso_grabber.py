import requests
import pandas as pd
import csv

class CSO_df:

    def __init__(self):
        print('Please vist https://data.cso.ie/ to get table codes')
        
    def get_cso_table(self, table_code):
        r = requests.get(f'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{table_code}/CSV/1.0/en')
        csvlst = list(csv.reader(r.text[3:].splitlines()))
        df = pd.DataFrame(csvlst[1:], columns=csvlst[0])
        df.VALUE = pd.to_numeric(df.VALUE)
        return df
