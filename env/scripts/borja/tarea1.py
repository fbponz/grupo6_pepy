#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:43:59 2020

@author: franciscodeborjaponz
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv('../../data/sales_dataset.csv', sep=',', decimal='.')
features = pd.read_csv('../../data/features_dataset.csv', sep=',', decimal='.')
stores = pd.read_csv('../../data/stores_dataset.csv', sep=',', decimal='.')

#QC OK
"""
Cuantitative Weekly Sales
"""
store_1_dept_1 = sales[((sales["Store"] == 1)&(sales["Dept"] == 1))]
week_sales_store_1 = store_1_dept_1["Weekly_Sales"]


week_sales_description = store_1_dept_1.Weekly_Sales.describe()

ticks = np.arange(week_sales_description["min"]-537,week_sales_description["max"]+7,((week_sales_description["max"]-week_sales_description["min"])/5))

mean_wsd = week_sales_description["mean"]
std_wsd = week_sales_description["std"]
number_wsd = week_sales_description["count"]

box_string = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(mean_wsd, std_wsd, number_wsd)
props = dict(boxstyle='round', facecolor='white', lw=0.5)

plt.hist(week_sales_store_1, edgecolor="black", color="green")

plt.xticks(ticks)
plt.xlabel("Week sales in dollars ($)")
plt.ylabel("Amount of weeks")
plt.title("Fig.1: Weekly sales in store 1(Dept 1) by amount of weeks" "\n" "2010-2012")
plt.text(47200, 45, box_string, bbox=props) 
plt.axvline(x=mean_wsd, linewidth=1, linestyle="solid", color="red", label="Mean")
plt.axvline(x=mean_wsd+std_wsd, linewidth=1, linestyle="dashed", color="blue", label="Mean + S.D")
plt.legend()
plt.show()

"""
Nominal Store Weekly_Sales
"""
temp_value = sales.reset_index().groupby('Store').Weekly_Sales.sum()
temp_value = temp_value.reset_index()
stores['Total_Sales'] = temp_value['Weekly_Sales']
del(temp_value)
tsps_descript = stores.Total_Sales.describe()

mean = tsps_descript[1]
std = tsps_descript[2]
count = tsps_descript[0]


mean_substract_std = mean - std
mean_add_std = mean + std

stores.loc[(stores['Total_Sales']<mean_substract_std), "class_sales"] = "1: Low sales"
stores.loc[((stores['Total_Sales']>=mean_substract_std)&(stores['Total_Sales']<mean_add_std)), "class_sales"] = "2: Average sales"
stores.loc[(stores['Total_Sales']>=mean_add_std), "class_sales"] = "3: High sales"

mytable = stores.groupby(['class_sales']).size()
count=mytable.sum()
mytable2= (mytable/count)*100


bar_list = ['Low sales', 'Average sales', 'High sales']
plt.bar(bar_list, mytable2, edgecolor="black", color='green')
plt.ylabel('Percentage')
plt.xlabel('range of sales')
plt.title('Figure 3: Percentage distribution based on total sales of each store')
plt.show()


"""
"""
store_1 = sales[sales["Store"] == 1]

total_sales = sales["Weekly_Sales"].sum()
num_total_dept = sales.Dept.unique()

total_dept_sales = []
bar_list = []
for handler in num_total_dept:
    temp = store_1.loc[store_1['Dept']==handler,'Weekly_Sales'].sum()
    if (0.1< ((temp/total_sales)*100)):
        total_dept_sales.append(temp)
        bar_list.append('Dpt'+str(handler))

mytable2 = (total_dept_sales/total_sales)*100

plt.bar(bar_list,mytable2)
plt.xlabel("Departament name")
plt.ylabel("Percentage over total sales")
plt.title("Figure 6: Deparments with sales above 10% on total sales")
plt.show()

"""
Rate $ of sale per each m2

stores['rate_dollars_per_m2'] = stores['Total_Sales']/stores['Size']
tsps_descript = stores.rate_dollars_per_m2.describe()

mean = tsps_descript[1]
std = tsps_descript[2]
count = tsps_descript[0]
stores.loc[(stores['rate_dollars_per_m2']<mean_substract_std), "rate_profit"] = "1: Low ROI"
stores.loc[((stores['rate_dollars_per_m2']>=mean_substract_std)&(stores['rate_dollars_per_m2']<mean_add_std)), "rate_profit"] = "2: Average ROI"
stores.loc[(stores['rate_dollars_per_m2']>=mean_add_std), "rate_profit"] = "3: High ROI"

mytable = stores.groupby(['rate_profit']).size()
count=mytable.sum()
mytable2= (mytable/count)*100


bar_list = ['Low ROI', 'Average ROI', 'High ROI']
plt.bar(bar_list, mytable2, edgecolor="black", color='green')
plt.ylabel('Percentage')
plt.xlabel('range of sales')
plt.title('Figure 3: Percentage distribution based on total sales of each store')
plt.show()"""
