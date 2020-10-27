#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:43:04 2020

@author: inesrosellquintanilla

21/10/2020
Descripción de variables: del dataset Retail Data Analytics, que contiene datos históricos sobre ventas de 45 tiendas.
"""

"""
The database Retail Data Analytics contains historical data for 45 stores (and each of their departmente) located in different regions. 
There are three different files containing different information, that can be merged by the store ID (identification number of each retail store). 
    1. Store: This file contains the following variables:
        - Store: Store identification number.
        - Type: A, B, o C.
        - Size: Expressed in square feet.
    2. Features: This file contains inforation related to the stores, the departments, and the regional activity.
        - Store: Store identification number.
        - Date: Week
        - Temperature: Average temperature in region.
        - Fuel_Price: Cost of fuel in the region
        - MarkDown1-5: Anonymized data related to promotional markdowns. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA
        - CPI: Consumer price index
        - Unemployment rate: The unemployment rate
        - IsHoliday: This variable indicates whether the week is a special holiday week.
     3. Sales: Historical sales data from 2010-02-05 to 2012-11-01:
         - Store: Store identification number.
         - Dept: Department identification number.
         - Date: Week
         - IsHoliday: This variable indicates whether the week is a special holiday week.

This data is useful to predict department-wide sales in the coming years, and to analyse the impact of mardowns on holiday weekes. 
The analysis could help in providing recommendations based on data to increase sales and adapt the business model to changing environments.

Below, we describe some of the variables (either nominal or cuantitative).

Del archivo stores vamos a explorar la variable nominal Type y la varibale cuantitativa size. 

"""
#reset -f
# 1. Cargamos las libraries

import os   ## Sistema operativo, gestión de archivos
import pandas as pd  ## Pandas nos permite tener dataframes en Python , permite que Python pueda gestionar matrices de datos y la importamos omo pd,pd es un nickname (utilizar los nicks standard)  
import numpy as np ## Numeric python para hacer operaciones de matrices y vectores
import matplotlib.pyplot as plt ## Para hacer gráficos

# 2. Indicamos el directorio de trabajo

os.chdir("/Users/inesrosellquintanilla/Documents/EDEM/grupo6_pepy/env/data")

# 3. Importamos el dataset 

stores= pd.read_csv ('stores_dataset.csv', sep=',', decimal='.') ##separador , y decimal . porque es csv de EEUU

# 4. Explorar si el dataframe se ha cargado correctamente
## El Dataframe tiene 45 filas, una por cada tienda, y 3 columnas (que hacen referencia a Store, Type, Size). 
## hacemos una análisis de los datos 

stores.shape
stores.head()
stores.tail() 

#QC OK

## 5. Descripción de variable nominal : Type
## Para describir la variable type, una variable nominal, hace falta saber el porcentaje que representa cada tipo de tienda sobre el total
## Esto lo haremos de dos formas diferentes. En primer lugar, mediante una tabla de frecuencias y porcentajes. Además, realizaremos una gráfico de barras
## en el que se vea claramente el porcentaje que representan cada uno de los tipos de tiendas.

# En primer lugar calculamos la frecuencia de cada tipo de tienda

mytable = stores.groupby(['Type']).size()
print(mytable)

## Porcentajes

mytable.sum()
n=mytable.sum()

mytable2= (mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)
mytable3

## Gráfico de barras

bar_list = ['A', 'B', 'C']
plt.bar(bar_list, mytable2, color='lightsteelblue')
plt.ylabel('Percentage')
plt.xlabel('Type of shop')
plt.title('Figure 1. Percentage distribution of type of shops')
plt.show()

# En el gráfico observamos que casi un 50% de las tiendas son de tipo A, mientras que menos de un 20% son de tipo C. Las tiendas tipo B representan alrededor del 40%


## 6. escripción de la variable cuantitativa Size. Esta variable nos indica el tamaño de cada tienda en sqare feet. Es una variable cuantitativa, por lo que para desribirla
#necestaremos obtener los descriptivos, y hacer un histogtama.
#Primero, obtenemos la tabla de descriptivos, y lo guardamos bajo el nombre res

res= stores.Size.describe()
print(res)

m=round(res[1],1)
sd=round(res[2],1)
n=res[0]

# A continuación, realizamos el histograma
# Variable a imprimir: Size

x=stores.Size

# Histograma
ticks=np.arange(0,280000,40000)
props=dict(boxstyle='round', facecolor= 'white', lw=0.5)
textstr='$\mathrm{n}=%.0f$'%(n)


plt.hist(x, edgecolor='grey', color='lightsteelblue', bins=8)
plt.xticks(ticks)
plt.title('Figure 2. Store size''\n' '           Square feet')
plt.ylabel('Frequency')
plt.xlabel('Stores size')
plt.text (10000,12, textstr, fontsize=8, bbox=props)
plt.axvline(x=m, linewidth=0.8, linestyle= 'solid', color="indianred", label='Mean')
plt.axvline(x=m-sd, linewidth=0.8, linestyle= 'dashed', color="darkseagreen", label='-1 SD')
plt.axvline(x=m+sd, linewidth=0.8, linestyle= 'dashed', color="darkseagreen", label='+1 SD')
plt.legend(loc='best', bbox_to_anchor=(0.79,0.95), fontsize=8)
plt.show()

## En el histograma observamos que la media de tamaño es igual a 130287.6, y la desviación típica es prácticamente 64.000, bastante elevada. En el histograma observamos mayoría de las tiendas tienen un tamaño cercano al tamaño máximo o mínio.