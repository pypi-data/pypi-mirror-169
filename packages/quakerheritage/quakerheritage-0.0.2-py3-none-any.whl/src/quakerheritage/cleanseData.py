import pandas as pd
import numpy as np

# collate all data
def createDataframe(dictList):
    data = []
    data.append([i for i in dictList[0].keys()])
    for dct in dictList:
        data.append([i for i in dct.values()])
    df = pd.DataFrame(data, columns = data[0])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    return df

#transform differing data to create consistentcy in the database 
def hygieneDataframe(df):
    df.rename(columns={'Historic Environment Scotland': 'Historic locality', 'Reference': 'Listing Reference'}, inplace = True)
    try:
        df['Listed status'] = df['Listed status'].apply(lambda x: 'Not listed' if 'No' in x else x)
        df['Listing Reference'] = df['Listing Reference'].apply(lambda x: 'N/A' if ('Not applicable' in x or x.upper() == 'N/A') else x)
        df['Heritage at Risk'] = np.where(df['Listed status'].str.upper() == 'NOT LISTED', 'No', df['Heritage at Risk'])
        df['Date'] = df['Date'].str.extract(r'^(\d{4})', expand=False)
        df['Architect'] = df['Architect'].replace({'Not established': 'Unknown', 'not established': 'Unknown', 'None': 'Unknown',',':';'}, regex = True)
        df['Name of contact made on site'] = df['Name of contact made on site'].replace(' and ', ';')
        df['Date of visit'] = pd.to_datetime(df['Date of visit']).apply(lambda x: x.date())
        df['Associated buildings and sites'] = df['Associated buildings and sites'].apply(lambda x: 'N/A' if ('Not applicable' in x or 'None' in x) else x)
    except:
        pass
    
    return df

def saveToCSV(df, filepath):
    df.to_csv(filepath, encoding='utf-8-sig')

def loadFromCSV(filepath):
    return pd.read_csv(filepath)