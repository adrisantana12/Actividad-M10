import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

kind = "bar"


df = pd.DataFrame()


df = pd.read_csv('/content/Tasa_de_Cambio_Representativa_del_Mercado-_TRM.csv', delimiter=',')

print(df)

print('La media es: ',df.VALOR.mean())

print('La mediana es: ',df.VALOR.median())

print('La desviacion estandar es:', df.VALOR.std())

print('El maximo es:', df.VALOR.max())

print('El minimo es:', df.VALOR.min() )

print('La varianza es:', df.VALOR.var())

print('El rango de toda la columna de valor es:' , pd.Series(df.VALOR))

print(df.VALOR.describe())

print(df.info())

print(df.VALOR.hist())

data = df.VALOR

pip install sodapy

import pandas as pd

from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

results = client.get("hzid-rku2")

#Crear un DataFrame a partir de la lista
lechebovina_df = pd.DataFrame.from_records(results)

#Mostrar los 10 primeros registros
print(lechebovina_df.head(10))

#Eliminar filas con datos nulos
lechebovina_df2 = lechebovina_df.copy() 

#Axis=0 debido a que se van a eliminar las filas que contengan
#valores nulos
lechebovina_df2 = lechebovina_df2.dropna(axis=0,how="any")

print(lechebovina_df2.isnull().sum())

print(len(lechebovina_df2))

lechebovina_df2[lechebovina_df2['aptitud']=="Aptitud alta"].groupby(lechebovina_df2['departamen']).count()[['departamen']]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(lechebovina_df.municipio,lechebovina_df.aptitud)
plt.show()

lechebovina_df.pivot_table(values="area_ha", index=["municipio"],columns=["aptitud"],aggfunc="count" )












