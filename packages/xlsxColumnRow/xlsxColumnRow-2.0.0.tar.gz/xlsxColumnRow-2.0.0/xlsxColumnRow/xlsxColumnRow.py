import json
import pandas as pd

def xlsxColumnRow(xlsxData):
    data = json.loads(xlsxData)
    df = pd.DataFrame.from_dict(data, orient='columns')
    columns = df.columns.values.tolist()
    tempValuesList=[]
    for column in columns:
        values = df[column]
        values= values.dropna()
        values = values.unique()
        values = values.tolist()
        tempValuesList.append(values)
    result = {}
    result['rowCount']=len(df)
    result['columnNames']=columns
    result['values']=tempValuesList
    return json.dumps(result)
