# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:15:07 2018

@author: Raffael
"""
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def gera_tabela(nome):
    infile = open(nome,'r')

    data = []
    prices = []

    lines = infile.readlines()
    first_line = lines[0]
    properties = first_line.split(',')

  
    for line in lines[1:]:
        words = line.split(',')
        data.append(datetime.strptime(words[0], '%Y-%m-%d'))
        prices.append(float(words[1]))
        
    prices = np.array(prices)
    
    return data, prices

datas = {}
precos = {}

for i in ['PROBLEM_AAPL.csv', 'PROBLEM_GOOG.csv', 'PROBLEM_MSFT.csv']:
    datas[i], precos[i] = gera_tabela(i)

a = datas['PROBLEM_GOOG.csv'][0]

for i in ['PROBLEM_AAPL.csv', 'PROBLEM_GOOG.csv', 'PROBLEM_MSFT.csv']:
    b = datas[i].index(a)
    precos[i] = precos[i]/precos[i][b]
    
fig, ax = plt.subplots()
for i in ['PROBLEM_GOOG.csv', 'PROBLEM_AAPL.csv', 'PROBLEM_MSFT.csv']:
    ax.plot_date(datas[i], np.log(precos[i]),'-', label=i)
    
plt.legend()
plt.ylabel('logarithm of normalized value')   
fig.autofmt_xdate()

