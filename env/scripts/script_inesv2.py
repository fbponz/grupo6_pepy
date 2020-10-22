#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:43:04 2020

@author: inesrosellquintanilla

21/10/2020
Descripción de variables: del dataset Retail Data Analytics, que contiene datos históricos sobre ventas de 45 tiendas.
"""

"""
La base de datos Retail Data Analytics contiene información sobre las ventas en 45 tiendas (retail stores) en diferentes regiones y sus respectivos departamentos. Hay 3 csv, con diferente información
que se pueden unir con el ID store (el númro de la tienda):
    1. Store: Contiene información sobre 
        - Store: Número identificador de la tienda
        - Type: A, B, o C.
        - Size: Tamaño de la tienda, en square feet.
    2. Features: Contiene información relacionada a la tienda, los departamentos, y la actividad regional 
        - Store: Número identificador de la tienda
        - Date: Semana
        - Temperature: Temperatura media en la región
        - Fuel_Price: Precio del combustible en la región.
        - MarkDown1-5: Datos anónimos relacionados con descuentos promocionales. Los datos sobre descuentos sólo están disponibles a partir de noviembre del 2011. 
          La información no está disponible para todas las tiendas en todas las fechas. Los missing values se denominan como NA.
        - CPI: Índice de precios al consumo. 
        - Unemployment rate: Tasa de paro
        - IsHoliday: Variable que identifica si la semana es una semana especial por vacaciones.
     3. Sales: Datos históricos sobre ventas, desde el 05/02/2005 hasta el 01/11/2011, donde encontramos los siguientes campos:
         - Store: Número identificador de la tienda.
         - Dept: Número identificador del departamento.
         - Date: Semana
         - Weekly_Sales: Ventas cada semana en un departamento determinado en una tienda determinada.
Este conjunto de datos nos sirve para predecir, en primer lugar, las ventas por departamento en cada tienda en años próximos. Además. podemos analizar el
impacto de los descuentos en las semanas de vacaciones, y así dar recomendaciones paor regiones y tiendas que tengan un impacto positivo en las ventas y en el modelo de negocio.

En este primer ejercicio, se describen diferentes variables del dataset, tanto nominales como cuantitativas. 

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
plt.ylabel('Porcentaje')
plt.xlabel('Tipo de tienda')
plt.title('Gráfico 1. Distribución porcentual de los tipos de tiendas')
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
plt.title('Gráfico 2. Tamaño de las tiendas''\n' '           Square feet')
plt.ylabel('Frecuencia')
plt.xlabel('Tamaño de las tiendas')
plt.text (10000,12, textstr, fontsize=8, bbox=props)
plt.axvline(x=m, linewidth=0.8, linestyle= 'solid', color="indianred", label='Mean')
plt.axvline(x=m-sd, linewidth=0.8, linestyle= 'dashed', color="darkseagreen", label='-1 SD')
plt.axvline(x=m+sd, linewidth=0.8, linestyle= 'dashed', color="darkseagreen", label='+1 SD')
plt.legend(loc='best', bbox_to_anchor=(0.79,0.95), fontsize=8)
plt.show()

## En el histograma observamos que la media de tamaño es igual a 130287.6, y la desviación típica es prácticamente 64.000, bastante elevada. En el histograma observamos mayoría de las tiendas tienen un tamaño cercano al tamaño máximo o mínio.