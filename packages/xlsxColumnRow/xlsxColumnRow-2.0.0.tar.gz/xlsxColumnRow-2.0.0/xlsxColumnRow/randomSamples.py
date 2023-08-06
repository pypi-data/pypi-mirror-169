
import json
import pandas as pd

def samples(randomData):
    inputData =  json.loads(randomData)
    noOfSamples = inputData['process']['totalNumberOfSamples']
    data = json.loads(inputData['dataString'])
    attributes = inputData['process']['attributes']
    df = pd.DataFrame.from_dict(data,orient='columns')
    indicator = True
    for attribute in attributes:
        lst = attribute['columnValue']
        columnName = attribute['columnName']
        count = attribute['noOfSamples']
        df1 = df[df[columnName].isin(lst)].sample(n=int(count),replace=True)
        if indicator:
            result = df1
            indicator=False 
        else:
            temp = [df1,result]
            result = pd.concat(temp)
        df.drop(df1.index)
    if len(result)<int(noOfSamples):
        temp2 = df.sample(n=int(noOfSamples)-len(result))
        temp3 = [temp2,result]
        result = pd.concat(temp3)
    return result.to_json(orient ='records')