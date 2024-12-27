# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:42:11 2024

@author: Vaggelis Grammenidis
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:14:18 2024

@author: Vaggelis Grammenidis
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import datetime
import pandas_datareader.data as web

#EXERCISE 1

DM = pd.read_excel('Dynamic_Macro_Part_I.xlsx')
print(DM)

DM['real_gdp'] = DM['rgdpbarro']*DM['pop']
print(DM['real_gdp'])

gdpgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rgdp = DM['real_gdp']

DM['GDP deflator'] = (DM['gdp']/DM['real_gdp'])*100

for t in range(151)[1:]:
    gdpgrowth[t]= ((rgdp[t] - rgdp[t-1])/rgdp[t-1])*100
    
print(gdpgrowth)

DM['consumption'] = DM['rconsbarro']*DM['pop']
cons = DM['consumption']

consgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    consgrowth[t]= ((cons[t] - cons[t-1])/cons[t-1])*100
   
DM['net_exports'] = (DM['exports'] - DM['imports'])/DM['GDP deflator']
nex = DM['net_exports']

nexgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    nexgrowth[t]= ((nex[t] - nex[t-1])/nex[t-1])*100
 
exp = DM['expenditure']
expgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    expgrowth[t]= ((exp[t] - exp[t-1])/exp[t-1])*100
  
DM['investment'] = DM['gdp']*DM['iy']
inv = DM['investment']

invgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    invgrowth[t]= ((inv[t] - inv[t-1])/inv[t-1])*100
 
unempl = DM['unemp']
unemplgrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    unemplgrowth[t]=((unempl[t] - unempl[t-1])/unempl[t-1])*100
 
wage = DM['wage']
wagegrowth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(151)[1:]:
    wagegrowth[t]= ((wage[t] - wage[t-1])/wage[t-1])*100    

  
df = pd.DataFrame(DM)
df = df.set_index('Date')
DM = df
  
sync = {
    'consumption': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'real_gdp': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
}

DM['consumption_growth'] = consgrowth
DM['gdp_growth'] = gdpgrowth

sync = pd.DataFrame(sync)
sync = sync.set_index(DM.index)
sync['consumption'] = DM['consumption_growth']
sync['real_gdp'] = DM['gdp_growth']
sync = sync.T 

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([0, 5000000])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 

g_params = {'alpha': 0.9}
b_params = {'color':'purple', 'alpha': 0.2}
t_params = {'color':'black', 'fontsize': 7, 
            'va':'top', 'ha':'center'}

rgdp.index = DM.index

ts = pd.Series(rgdp, index=DM.index)
cycle, trend = sm.tsa.filters.hpfilter(ts, lamb=100)  

sync = sync.T
sync['rgdp'] = rgdp
sync['trend'] = trend
sync['gdptrend'] = trend
sync = sync.T

fig, ax = plt.subplots()
variables = ['rgdp', 'trend']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)
plt.show()

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    # Highlight recessions
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([0, 5000000])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 

cons.index = DM.index

ts = pd.Series(cons, index=DM.index)
cycle, trend = sm.tsa.filters.hpfilter(ts, lamb=100)  # lambda is a smoothing parameter

sync = sync.T
sync['cons'] = cons
sync['trend'] = trend
sync = sync.T

fig, ax = plt.subplots()
variables = ['cons', 'trend', 'rgdp', 'gdptrend']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)
plt.show()

DM['unemployment_growth'] = unemplgrowth

DM['wage_growth'] = wagegrowth

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([-2800, 2800])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 

nex.index = DM.index

ts = pd.Series(nex, index=DM.index)
cycle, trend = sm.tsa.filters.hpfilter(ts, lamb=100)  

sync = sync.T
sync['nex'] = nex
sync['trend'] = trend
sync = sync.T

fig, ax = plt.subplots()
variables = ['nex', 'trend','rgdp', 'gdptrend']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)
plt.show()

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([0, 55000000])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 


inv.index = DM.index

ts = pd.Series(inv, index=DM.index)
cycle, trend = sm.tsa.filters.hpfilter(ts, lamb=100) 

sync = sync.T
sync['inv'] = inv
sync['trend'] = trend
sync = sync.T

fig, ax = plt.subplots()
variables = ['inv', 'trend','rgdp', 'gdptrend']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)
plt.show()

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([0, 50000000])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 


exp.index = DM.index
for t in range(1939)[1936:]:
    exp[t] = exp[1935]
exp[1939] = exp[1940]

ts = pd.Series(exp, index=DM.index)
cycle, trend = sm.tsa.filters.hpfilter(ts, lamb=100) 

sync = sync.T
sync['exp'] = exp
sync['trend'] = trend
sync = sync.T

fig, ax = plt.subplots()
variables = ['exp', 'trend','rgdp', 'gdptrend']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)
plt.show()

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-100, 100])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

DM['gdp_growth'] = gdpgrowth

date = DM.index
ylabel = 'Real GDP growth rate (%)'
plot_series(DM['gdp_growth'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-100, 100])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

DM['consumption_growth'] = consgrowth

date = DM.index
ylabel = 'Consumption growth rate (%)'
plot_series(DM['consumption_growth'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-100, 100])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

DM['investment_growth'] = invgrowth

date = DM.index
ylabel = 'Investment growth rate (%)'
plot_series(DM['investment_growth'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-100, 100])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

DM['expenditure_growth'] = expgrowth

date = DM.index
ylabel = 'Expenditure growth rate (%)'
plot_series(DM['expenditure_growth'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-1000, 1000])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

DM['net_exports_growth'] = nexgrowth

date = DM.index
ylabel = 'Net Exports growth rate (%)'
plot_series(DM['net_exports_growth'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

#EXERCISE 2

inflation = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DM['inflation'] = inflation
for t in range(2020)[1871:]:
    DM['inflation'][t] = ((DM['cpi'][t] - DM['cpi'][t-1])/DM['cpi'][t-1])*100
    
DM['M1 growth'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(2020)[1871:]:
    DM['M1 growth'][t] = ((DM['narrowm'][t] - DM['narrowm'][t-1])/DM['narrowm'][t-1])*100
  
DM['M2 growth'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(2020)[1871:]:
    DM['M2 growth'][t] = ((DM['money'][t] - DM['money'][t-1])/DM['money'][t-1])*100

k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DM['constant k M1'] = k
DM['constant k M1'] = DM['narrowm']/(DM['cpi']*DM['real_gdp'])

DM['constant k M2'] = k
DM['constant k M2'] = DM['money']/(DM['cpi']*DM['real_gdp'])

def plot_series(data, variables, ylabel, 
                txt_pos, ax, g_params,
                b_params, t_params, ylim=15, baseline=0):
    ax.plot(data.loc[variables], label=variables, **g_params)

    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if ylim != None:
        ax.set_ylim([-25, 50])
    else:
        ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos,
            'Great depression\n(1929)', **t_params)     
    ax.text(1974, ylim + ylim*txt_pos,
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos,
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos,
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos,
            'Covid-19\n(2020)', **t_params)

fig, ax = plt.subplots()

date = DM.index
ylabel = 'Change in CPI over time (%)'
plot_series(DM['inflation'], date,
            ylabel, 0.1, ax, 
            g_params, b_params, t_params)
plt.show()

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([-20, 100])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 
    if baseline != None:
        ax.hlines(y=baseline, xmin=ax.get_xlim()[0], 
                  xmax=ax.get_xlim()[1], color='black', 
                  linestyle='--')
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax

sync = sync.T
sync['inflation'] = DM['inflation']
sync['M1'] = DM['M1 growth']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'M1']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.1, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['M2'] = DM['M2 growth']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'M2']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1870:],  
                variables, ylabel,
                0.1, 40, ax, 
                g_params, b_params, t_params)

DM['kM1t1'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for t in range(2020)[1870:]:
    DM['kM1t1'][t] = DM['constant k M1'][1870]
DM['kM1t1'][2020] = DM['constant k M1'][1870]    

for t in range(1998)[1874:]:
    DM['kM1t1'][t] = DM['constant k M1'][t]    
    
DM['kM1t2'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for t in range(2020)[1870:]:
    DM['kM1t2'][t] = DM['constant k M1'][1870]
DM['kM1t2'][2020] = DM['constant k M1'][1870] 

for t in range(2020)[1999:]:
    DM['kM1t2'][t] = DM['constant k M1'][t]

DM['kM2t1'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for t in range(2020)[1870:]:
    DM['kM2t1'][t] = DM['constant k M1'][1870]
DM['kM2t1'][2020] = DM['constant k M1'][1870]    

for t in range(1978)[1874:]:
    DM['kM2t1'][t] = DM['constant k M2'][t]    
    
DM['kM2t2'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for t in range(2020)[1870:]:
    DM['kM2t2'][t] = DM['constant k M1'][1870]
DM['kM2t2'][2020] = DM['constant k M1'][1870] 

for t in range(1996)[1979:]:
    DM['kM2t2'][t] = DM['constant k M2'][t]
    
DM['kM2t3'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for t in range(2020)[1870:]:
    DM['kM2t3'][t] = DM['constant k M1'][1870]
DM['kM2t3'][2020] = DM['constant k M1'][1870] 

for t in range(2020)[1997:]:
    DM['kM2t3'][t] = DM['constant k M2'][t] 
    
def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([0, 25])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 

sync = sync.T
sync['k M1 1874 - 1998'] = DM['kM1t1']*100
sync['k M1 1999 - 2020'] = DM['kM1t2']*100
sync = sync.T

fig, ax = plt.subplots()
variables = ['k M1 1874 - 1998', 'k M1 1999 - 2020']
ylabel = 'Quantity Theory of Money'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['k M2 1874 - 1978'] = DM['kM2t1']*100
sync['k M2 1979 - 1996'] = DM['kM2t2']*100
sync['k M2 1997 - 2020'] = DM['kM2t3']*100
sync = sync.T

fig, ax = plt.subplots()
variables = ['k M2 1874 - 1978', 'k M2 1979 - 1996', 'k M2 1997 - 2020']
ylabel = 'Quantity Theory of Money'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.08, 40, ax, 
                g_params, b_params, t_params)

DM['thh percentage'] = (DM['thh']/DM['tloans'])*100

DM['tbus percentage'] = (DM['tbus']/DM['tloans'])*100

DM['tmort percentage'] = (DM['tmort']/DM['tloans'])*100

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([-100, 100])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 
    if baseline != None:
        ax.hlines(y=baseline, xmin=ax.get_xlim()[0], 
                  xmax=ax.get_xlim()[1], color='black', 
                  linestyle='--')
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax

sync = sync.T
sync['thh perc'] = DM['thh percentage']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'thh perc']
ylabel = 'inflation-thh percentage corrolation (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['tbus perc'] = DM['tbus percentage']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'tbus perc']
ylabel = 'inflation-tbus percentage corrolation (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['tmort perc'] = DM['tmort percentage']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'tmort perc']
ylabel = 'inflation-tmort percentage corrolation (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)

    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([-25, 350000000])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 

sync = sync.T
sync['total loans'] = DM['tloans']
sync = sync.T

fig, ax = plt.subplots()
variables = ['inflation', 'total loans']
ylabel = 'inflation-total loans corrolation (%)'
plot_comparison(sync.loc[variables, 1870:], 
                variables, ylabel,
                0.1, 40, ax, 
                g_params, b_params, t_params)

#Exercise 3

DM['public_debt'] = DM['debtgdp']*DM['real_gdp']

B = DM['public_debt']

DM['z_parameter'] = (1+DM['stir']+DM['ltrate'])/((1+DM['gdp_growth'])+(1+DM['inflation']))

DM['interest rate'] = DM['stir'] + DM['ltrate']

Yaxis = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

R = 0
for t in range(2020)[1940:]:
    R = R + DM['z_parameter'][t]

fig, axs = plt.subplots(4, 1, figsize=(10, 6))


axs[0].plot(DM.index, DM['inflation'], color='blue', label='inflation')
axs[0].plot(DM.index, DM['interest rate'], color='red', label='interest rate')
axs[0].plot(DM.index, DM['gdp_growth'], color='green', label='GDP growth')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('1')
axs[0].legend()

axs[1].plot(DM.index, DM['z_parameter'], color='blue', label='z parameter')
axs[1].plot(DM.index, Yaxis, color='orange', label='Y = 1')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('2')
axs[1].legend()

axs[2].plot(DM.index, DM['debtgdp'], color='blue', label='Public Debt to GDP')
axs[2].set_xlabel('Year')
axs[2].set_ylabel('3')
axs[2].legend()

axs[3].plot(DM.index, DM['public_debt'], color='blue', label='Public Deficit')
axs[3].set_xlabel('Year')
axs[3].set_ylabel('4')
axs[3].legend()

DM['public debt growth'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for t in range(2020)[1871:]:
    DM['public debt growth'][t] = ((DM['debtgdp'][t] - DM['debtgdp'][t-1])/DM['debtgdp'][t-1])*100

sync = sync.T
sync['publicdebt'] = DM['public debt growth']
sync = sync.T

def plot_comparison(data, variables, 
                        ylabel, txt_pos, y_lim, ax, 
                        g_params, b_params, t_params, 
                        baseline=0):

    for variable in variables:
        ax.plot(data.loc[variable], label=variable, **g_params)
    
    ax.axvspan(1929, 1932, **b_params)
    ax.axvspan(1973, 1975, **b_params)
    ax.axvspan(1990, 1992, **b_params)
    ax.axvspan(2007, 2009, **b_params)
    ax.axvspan(2019, 2021, **b_params)
    if y_lim != None:
        ax.set_ylim([-100, 100])
    ylim = ax.get_ylim()[1]
    ax.text(1929, ylim + ylim*txt_pos, 
            'Great depression\n(1929)', **t_params) 
    ax.text(1974, ylim + ylim*txt_pos, 
            'Oil Crisis\n(1974)', **t_params) 
    ax.text(1991, ylim + ylim*txt_pos, 
            '1990s recession\n(1991)', **t_params) 
    ax.text(2008, ylim + ylim*txt_pos, 
            'GFC\n(2008)', **t_params) 
    ax.text(2020, ylim + ylim*txt_pos, 
            'Covid-19\n(2020)', **t_params) 
    if baseline != None:
        ax.hlines(y=baseline, xmin=ax.get_xlim()[0], 
                  xmax=ax.get_xlim()[1], color='black', 
                  linestyle='--')
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax

sync = sync.T
sync['unemployment'] = DM['unemployment_growth']
sync = sync.T

fig, ax = plt.subplots()
variables = ['unemployment', 'real_gdp']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['wage'] = DM['wage_growth']
sync = sync.T

fig, ax = plt.subplots()
variables = ['unemployment', 'wage']
ylabel = 'GDP growth rate (%)'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

fig, ax = plt.subplots()
variables = ['wage', 'real_gdp']
ylabel = 'Growth rates (%)'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

fig, ax = plt.subplots()
variables = ['inflation', 'wage']
ylabel = 'inflation-wage corrolation (%)'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

fig, ax = plt.subplots()
variables = ['inflation', 'unemployment']
ylabel = 'inflation-unemployment corrolation (%)'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

sync = sync.T
sync['public debt'] = DM['public debt growth']
sync = sync.T

fig, ax = plt.subplots()
variables = ['public debt', 'wage']
ylabel = 'Public debt growth to Wage growth'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

fig, ax = plt.subplots()
variables = ['public debt', 'unemployment']
ylabel = 'Public debt growth to Unemployment growth'
plot_comparison(sync.loc[variables, 1939:], 
                variables, ylabel,
                0.2, 40, ax, 
                g_params, b_params, t_params)

