import pandas as pd
import json
import random
from src.funapi import llamaApi

def filtro(mes,distrito):
    df=pd.read_csv('input/accidentes2018.csv', engine='python')
    df=df[(df['MES']==mes) & (df['DISTRITO']==distrito)]
    return df
def asignaTemplo(distrito):
    respuesta=json.load(llamaApi(distrito))
    listaiglesias=[]
    for t in respuesta['@graph']:
        listaiglesias.append(t['title'])
    ig=random.choice(listaiglesias)
    return ig
def columnaDivina(dataframe):
    dataframe['DIOS OS ESPERABA EN:'] = dataframe['DISTRITO'].apply(asignaTemplo)
    return dataframe
def limpiaFinal(dataframe):
    return dataframe[['FECHA','LUGAR DEL ACCIDENTE','NUM VICTIMAS','DIOS OS ESPERABA EN:']].reset_index()