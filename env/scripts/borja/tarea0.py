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

sales_dataset = pd.read_csv('../../data/sales_dataset.csv', sep=',', decimal='.')
#QC OK
"""
Cuantitativa
"""
store_1_dept_1 = sales_dataset[((sales_dataset["Store"] == 1)&(sales_dataset["Dept"] == 1))]
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
