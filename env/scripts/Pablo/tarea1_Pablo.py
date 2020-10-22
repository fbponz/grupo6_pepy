# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%reset -f
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
"""
Features --> Fuel_price, isHoliday
Sales
"""
#%%
os.getcwd()
os.chdir("/Users/penades/Desktop/MDA/grupo6_pepy/grupo6_pepy/env/scripts/Pablo")

#Load Retail csvs
features = pd.read_csv("/Users/penades/Desktop/MDA/grupo6_pepy/grupo6_pepy/env/data/features_dataset.csv")
sales = pd.read_csv("/Users/penades/Desktop/MDA/grupo6_pepy/grupo6_pepy/env/data/sales_dataset.csv")
stores = pd.read_csv("/Users/penades/Desktop/MDA/grupo6_pepy/grupo6_pepy/env/data/stores_dataset.csv")
 

#QC
features.shape
features.head()
features.tail()
sales.shape
sales.head()
sales.tail()
stores.shape
stores.head()
stores.tail()
#QC OK

#%%
#####STATISTICS
#Quantitative variable Fuel_Price
features.Fuel_Price.describe() 
fuel_price_stats = features.Fuel_Price.describe()

m = fuel_price_stats[1]
s = fuel_price_stats[2]
n = fuel_price_stats[0]
x = features["Fuel_Price"]
plt.hist(x, edgecolor="black", color="gray")
ticks = np.arange(0,6,0.5)
plt.xticks(ticks)
plt.xlabel("Fuel price in dollars ($)")
plt.ylabel("Amount of days")
plt.title("Fig.1: Fuel price by amount of days" "\n" "2010-2012")
textstr = "Mean = 3.41\nS.D. = 0.43\nn = 8190" #texto a imprimir
props = dict(boxstyle="round", facecolor="white", lw=0.5) #Creamos un recuadro
plt.text(4.25, 1500, textstr, bbox=props) #texto en esa posicion
plt.axvline(x=m, linewidth=1, linestyle="solid", color="red", label="Mean")
plt.axvline(x=m-s, linewidth=1, linestyle="solid", color="green", label="S.D." )
plt.axvline(x=m+s, linewidth=1, linestyle="solid", color="green", label="-S.D." )
#plt.legend()
plt.show()
print("""As expected, the fluctuation of fuel prices is not considerably large. 
The mean lies at 3.41$ and the standard deviation is 0.43. Nevertheless, 
the most frequent price was around 3.65$.""")
print()#Blank line

#Nominal variable isHoliday
features.IsHoliday.describe()
IsHoliday_stats = features.IsHoliday.describe() 
y = features["IsHoliday"]
holiday_freq = features.groupby(["IsHoliday"]).size()
holiday_freq.sum()
n = holiday_freq.sum()
holiday_freq2 = (holiday_freq/n)*100
holiday_freq3 = round(holiday_freq2)
bar_list = ["Working", "Holiday"]
plt.bar(bar_list,holiday_freq2)
plt.xlabel("Type of day")
plt.ylabel("Percentage")
plt.title("Fig.2: Percentage of working days and holidays" "\n" "from 2010 to 2013")
plt.show()
print("""Only over 7% of the days are holidays. Nonetheless, the dataset starts 
in February and ends in July. Therefore, such number does not fully reflect the 
absolute amount of holidays in a year.""")