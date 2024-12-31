##Single Python document
##Business Cycle analysis, Monetary Aggregates Analysis and Fiscal Sustainability Analysis for the 
##United Kingdom
##Ilias Balatsouras, Economics Student from AUEB, as a part of the Dynamic Macroeconomics Project
##################Business Cycles#########################
##########################################################
import pandas as pd  
import matplotlib.pyplot as plt 
from statsmodels.tsa.filters.hp_filter import hpfilter
import gdown

# Google Sheets file ID extracted from the link
file_id = '16AezESYcXFx94KtyxPbYEyXqpJYnuEL7'

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file as an Excel file
output = 'part1_data_cleared.xlsx'
gdown.download(url, output, quiet=False)

# Load the Excel file
data_uk = pd.read_excel(output, engine='openpyxl')

# Extract columns
rgdp = data_uk['REAL_GDP (MILLION_POUNDS)']
rcons = data_uk['REAL_CONS (BARRO)']
i_to_gdp = data_uk['Investment to GDP Ratio']
debt_to_gdp = data_uk['DEBT TO GDP']
unemployment = data_uk['Unemployment']
time = data_uk['YEAR']
investment_abs = rgdp * i_to_gdp

rgdp_growth = [0]
for i in range(1, len(time)):
    new = (rgdp[i] - rgdp[i-1]) / rgdp[i-1]
    rgdp_growth.append(new)

plt.figure()
plt.plot(time, rgdp_growth, label='Real GDP growth rate')
plt.axhline(y=0, color='black', linestyle='--', label='y = 0')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Time')
plt.ylabel('Growth Rate')
plt.title('UK: Real GDP Growth Rate over Time')
plt.legend()
plt.show()

plt.figure()
plt.plot(time, rgdp)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real GDP Per Capita (Million Pounds)')
plt.title("UK's Real GDP Per Capita over time")
plt.show()

plt.figure()
plt.plot(time, rcons)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real Consumption Expenditure Per Capita (Million Pounds)')
plt.title("UK's Real Consumption Expenditure Per Capita over time")
plt.show()

plt.figure()
plt.plot(time, i_to_gdp)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Investment to GDP ratios over time')
plt.title('UK: Investment to GDP ratios')
plt.show()

plt.figure()
plt.plot(time, investment_abs)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Investment')
plt.title('UK: Investment over time')
plt.show()

plt.figure()
plt.plot(time, debt_to_gdp)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Debt to GDP Ratio (%)')
plt.title("UK's Debt to GDP Ratio over time")
plt.show()

plt.figure()
plt.plot(time, unemployment)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Unemployment')
plt.title("UK's Unemployment rate over time")
plt.show()

plt.figure()
plt.plot(time, rgdp, label='Real GDP Per Capita (Million Pounds)')
plt.plot(time, rcons, label='Real Consumption Per Capita (Million Pounds)')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('UK: Real GDP per capita, Real Consumption per capita')
plt.legend()
plt.show()

gdp_cycle, gdp_trend = hpfilter(rgdp, lamb=100)

plt.figure()
plt.plot(time, rgdp, color='blue', label='Real GDP')
plt.plot(time, gdp_trend, color='orange', label='Trend')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('GDP/ GDP components')
plt.title('Real GDP, Trend and Cycle')  
plt.legend()
plt.show()

plt.figure()
plt.plot(time, gdp_cycle, label='GDP cycle')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Time')
plt.ylabel('GDP Cycle')
plt.title('UK: GDP Cycle over Time')
plt.legend()
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, rgdp, label='Real GDP per capita')
plt.plot(time, gdp_trend, label="Trend of Real GDP per capita")
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real GDP')
plt.title('UK: Real GDP and Consumption over Time (Per Capita)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, rcons, label='Real Consumption Expenditure Per Capita')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real Consumption Per Capita')
plt.legend()
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, rgdp, label='Real GDP Per Capita')
plt.plot(time, gdp_trend, label="Trend of Real GDP Per Capita")
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real GDP Per Capita')
plt.title('UK: Real GDP and Debt to GDP over Time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, debt_to_gdp, label="Debt to GDP")
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Debt to GDP')
plt.legend()
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, rgdp, label='Real GDP Per Capita')
plt.plot(time, gdp_trend, label="Trend of Real GDP")
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real GDP Per Capita')
plt.title('UK: Real GDP and Unemployment Over Time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, unemployment, label='Unemployment Rate')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Unemployment')
plt.legend()
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, rgdp, label='Real GDP Per Capita')
plt.plot(time, gdp_trend, label='Trend of Real GDP Per Capita')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Real GDP Per Capita')
plt.title('UK: GDP Per Capita and Investment over time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, investment_abs, label='Investment')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Investment')
plt.legend()
plt.show()

plt.figure()
debt_abs = debt_to_gdp * rgdp
plt.plot(time, debt_abs, label='Debt (Absolute)')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Debt')
plt.title('UK: Debt over time')
plt.legend()
plt.show()



###################Monetary Cycles################################
##################################################################
import gdown

# Google Sheets file ID extracted from the link
file_id = '1mcsrQIeR8J03c_h742Q6Re6_CgzYqFOq'

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file as an Excel file
output = 'DATA_MACR0HISTORY_REVISED.xlsx'
gdown.download(url, output, quiet=False)

# Load the Excel file
data = pd.read_excel(output)

# Process the data
time = data['year']
narrow = data['narrowm']
broad = data['money']
stir = data['stir']
ltrate = data['ltrate']
bonds = data['bond_rate']
cpi = data['cpi']

# Calculate inflation
inflation = [(cpi[i] - cpi[i - 1]) / cpi[i - 1] for i in range(1, len(cpi))]
time_for_growth = time[1:]
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, stir, label='Short Term Interest Rates')
plt.xlabel('time')
plt.ylabel('Short Term Rates')
plt.title('UK: Short Term Interest Rates and Broad/Narrow Money')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, broad, label='Broad Money')
plt.xlabel('time')
plt.ylabel('Money Measures')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, stir, label='Short Term Interest Rates')
plt.xlabel('time')
plt.ylabel('Short Term Rates')
plt.title('UK: Short Term Interest Rates and Broad/Narrow Money')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, narrow, label='Narrow Money')
plt.xlabel('time')
plt.ylabel('Money Measures')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

perc_narrow = [(narrow[i] - narrow[i - 1]) / narrow[i - 1] for i in range(1, len(narrow))]
perc_broad = [(broad[i] - broad[i - 1]) / broad[i - 1] for i in range(1, len(broad))]

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_for_growth, perc_narrow, label='Narrow')
plt.xlabel('time')
plt.ylabel('Percentage Change')
plt.title('UK: % change of the Narrow/Broad Money')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time_for_growth, perc_broad, label='Broad')
plt.xlabel('time')
plt.ylabel('Percentage Change')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

narrow_cycle, narrow_trend = hpfilter(narrow, lamb=100)
broad_cycle, broad_trend = hpfilter(broad, lamb=100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, narrow_trend, label='Trend')
plt.xlabel('time')
plt.ylabel('Narrow Money')
plt.title('UK: Trend of the Monetary Measures')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, broad_trend, label='Trend')
plt.xlabel('time')
plt.ylabel('Broad Money')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, narrow_cycle, label='Narrow')
plt.xlabel('time')
plt.ylabel('Narrow Money')
plt.title('UK: Cyclical Components of the Monetary Measures')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, broad_cycle, label='Broad')
plt.xlabel('time')
plt.ylabel('Broad Money')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_for_growth, inflation, label='Inflation')
plt.xlabel('time')
plt.ylabel('Inflation')
plt.title('UK: Inflation and Interest Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)

plt.subplot(2, 1, 2)
plt.plot(time, stir, label='Short Term Rates')
plt.xlabel('time')
plt.ylabel('Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_for_growth, inflation, label='Inflation')
plt.xlabel('time')
plt.ylabel('Inflation')
plt.title('UK: Inflation and Interest Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)

plt.subplot(2, 1, 2)
plt.plot(time, ltrate, label='Long Term Rates')
plt.xlabel('time')
plt.ylabel('Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()


plt.figure()
plt.plot(time, bonds, label='Bond Rates')
plt.xlabel('time')
plt.ylabel('Bond Rates')
plt.title('UK: Bond Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(time, bonds, label='Government Bond Rates', color='black')
plt.xlabel('time')
plt.ylabel('Bond Rates')
plt.title('UK: Government Bond Yields and Short Term Interest Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, stir, label='Short Term Interest Rates')
plt.xlabel('time')
plt.ylabel('Short Term Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(time, bonds, label='Government Bond Rates')
plt.xlabel('time')
plt.ylabel('Bond Rates')
plt.title('UK: Government Bond Yields and Long Term Interest Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, ltrate, label='Long Term Interest Rates')
plt.xlabel('time')
plt.ylabel('Long Term Rates')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 8))
axs[0].plot(time, bonds, label='Government Bond Rates')
axs[0].set_ylabel('Bond Rates')
axs[0].set_title('UK: Government Bond Yields and Interest Rates')
axs[0].legend()
axs[0].grid(True, which='both', linestyle='--', alpha=0.7)

axs[1].plot(time, stir, label='Short Term Interest Rates')
axs[1].set_ylabel('Short Term Rates')
axs[1].legend()
axs[1].grid(True, which='both', linestyle='--', alpha=0.7)

axs[2].plot(time, ltrate, label='Long Term Interest Rates')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Long Term Rates')
axs[2].legend()
axs[2].grid(True, which='both', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


############################Fiscal Sustainability############################
#############################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gdown

# Google Sheets file ID extracted from the link
file_id = '1MLVYZVx3vwJUw1wa-XWz3uLESLbkYsVx'

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file as an Excel file
output = 'DATA_CLEARED_VOL2.xlsx'
gdown.download(url, output, quiet=False)

# Load the Excel file
data_sub = pd.read_excel(output)

# Extract data
time = data_sub['TIME']
rgdp = data_sub['RGDP']
debt_to_gdp = data_sub['DEBT_TO_GDP']
revenue = data_sub['GOV_REVENUE']
expenditures = data_sub['GOV_EXP']
cpi = data_sub['CPI']
bond_rates = data_sub['BOND_RATE']

base_value = cpi.iloc[70]
deflator = cpi / base_value

inflation = [cpi[i] / cpi[i - 1] for i in range(1, len(time))]
rgdp_growth = [rgdp[i] / rgdp[i - 1] for i in range(1, len(time))]
gross_interest = np.array(bond_rates[1:])
rgdp_growth = np.array(rgdp_growth)
inflation = np.array(inflation)
gross_interest=gross_interest+1
rgdp_growth=rgdp_growth
inflation=inflation
zeta = gross_interest/(rgdp_growth*inflation)

ngdp = deflator * rgdp
deficit = expenditures - revenue
def_to_gdp = deficit / ngdp

plt.figure()
plt.plot(time, debt_to_gdp, label='Debt (% of GDP)', color='black')
plt.xlabel('Time')
plt.ylabel('Debt to GDP')
plt.title('UK: Debt to GDP Ratio')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, deficit, label='Deficit')
plt.xlabel('Time')
plt.ylabel('Deficits')
plt.title('UK: Deficits and Deficit to GDP Ratio')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, def_to_gdp, label='Deficit to GDP')
plt.xlabel('Time')
plt.ylabel('Deficit (% of GDP)')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

public_debt = debt_to_gdp * ngdp
delta_debt = [0] + [debt_to_gdp[i] - debt_to_gdp[i - 1] for i in range(1, len(time))]
def_to_debt = deficit / delta_debt

plt.figure()
plt.plot(time, def_to_debt, label='Deficit % of ΔDebt')
plt.xlabel('Time')
plt.ylabel('Deficit to Debt Ratio')
plt.title('UK: Deficit as % of Total Debt Change')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(max(def_to_debt))
print(min(def_to_debt))

revenue_to_gdp = revenue / ngdp
expenditure_to_gdp = expenditures / ngdp

plt.figure()
plt.plot(time, revenue_to_gdp, label='Revenue (% of GDP)')
plt.plot(time, expenditure_to_gdp, label='Expenditure (% of GDP)', linestyle='dotted', color='black')
plt.xlabel('Time')
plt.ylabel('Expenditures/Revenues (% of GDP)')
plt.title('UK: Expenditures and Revenues as % of GDP')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, def_to_gdp, label='Deficit (% of GDP)')
plt.xlabel('Time')
plt.ylabel('Deficit to GDP')
plt.title('UK: Deficit and Revenues/Expenditures (% of GDP)')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, revenue_to_gdp, label='Revenue (% of GDP)')
plt.plot(time, expenditure_to_gdp, label='Expenditure (% of GDP)', linestyle='dotted',)
plt.xlabel('Time')
plt.ylabel('Expenditures/Revenues (% of GDP)')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

time_new = time[1:]
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, debt_to_gdp, label='Debt (% of GDP)')
plt.xlabel('Time')
plt.ylabel('Debt to GDP')
plt.title('UK: Debt to GDP Ratio and Inflation Rate')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time_new, inflation, label='Inflation')
plt.xlabel('Time')
plt.ylabel('Inflation Rate')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.plot(time_new, zeta, label='(1+r)/[(1+π)+(1+γ)]')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('UK: Zeta Parameter Over Time')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1, color='black', linestyle='--', linewidth=1)
plt.ylim([min(zeta), max(zeta)])
plt.show()

debt_growth = [(debt_to_gdp[i] - debt_to_gdp[i - 1]) / debt_to_gdp[i - 1] for i in range(1, len(time))]

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, debt_to_gdp, label="Debt (% of GDP)")
plt.xlabel('Time')
plt.ylabel('Debt to GDP')
plt.title('UK: Debt to GDP -- Zeta Parameter')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time_new, zeta, label='Zeta Parameter')
plt.xlabel('Time')
plt.ylabel('Zeta')
plt.legend()
plt.axhline(y=1, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim([min(zeta), max(zeta)])
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_new, debt_growth, label='Debt to GDP Growth')
plt.xlabel('Time')
plt.ylabel('Debt to GDP Growth')
plt.title('UK: Debt to GDP Growth Rate and Zeta Parameter')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time_new, zeta, label='Zeta Parameter')
plt.xlabel('Time')
plt.ylabel('Zeta')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim([min(zeta), max(zeta)])
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, public_debt, label="Debt (% of GDP)")
plt.xlabel('Time')
plt.ylabel('Public Debt')
plt.title('UK: Debt -- Zeta Parameter')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time_new, zeta, label='Zeta Parameter')
plt.xlabel('Time')
plt.ylabel('Zeta')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim([min(zeta), max(zeta)])
plt.show()


#Construct a plot with several subplots for the trends and actual data
rcons_cycle, rcons_trend = hpfilter(rcons, lamb=100)
inv_cycle, inv_trend = hpfilter(investment_abs, lamb=100)
unem_cycle, unem_trend = hpfilter(unemployment, lamb=100)

fig, axs = plt.subplots(3, 2, figsize=(12, 10), sharex=True)

# Plot GDP
axs[0, 0].plot(time, gdp_trend, 'r--', label='GDP Trend')
axs[0, 0].plot(time, rgdp, 'b-', label='GDP Data')
axs[0, 0].set_title('GDP Trend vs Actual Data')
axs[0, 0].set_ylabel('Real GDP')
axs[0, 0].legend(loc='upper left')
axs[0, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Real Consumption
axs[0, 1].plot(time, rcons, 'b-', label='Real Consumption Data')
axs[0, 1].plot(time, rcons_trend, 'r--', label='Real Consumption Trend')
axs[0, 1].set_title('Consumption Trend vs Data')
axs[0, 1].set_ylabel('Consumption')
axs[0, 1].legend(loc='upper left')
axs[0, 1].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Investment
axs[1, 0].plot(time, investment_abs, 'b-', label='Investment Data')
axs[1, 0].plot(time, inv_trend, 'r--', label='Investment Trend')
axs[1, 0].set_title('Investment Trend vs Data')
axs[1, 0].set_ylabel('Investment')
axs[1, 0].legend(loc='upper left')
axs[1, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Unemployment
axs[1, 1].plot(time, unemployment, 'b-', label='Unemployment Data')
axs[1, 1].plot(time, unem_trend, 'r--', label='Unemployment Trend')
axs[1, 1].set_title('Unemployment Trend vs Data')
axs[1, 1].set_ylabel('Unemployment')
axs[1, 1].legend(loc='upper left')
axs[1, 1].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Narrow Money
axs[2, 0].plot(time, narrow, 'b-', label='Narrow Money Data')
axs[2, 0].plot(time, narrow_trend, 'r--', label='Narrow Money Trend')
axs[2, 0].set_title('Narrow Money Trend vs Data')
axs[2, 0].set_ylabel('Narrow Money')
axs[2, 0].set_xlabel('Time')
axs[2, 0].legend(loc='upper left')
axs[2, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Broad Money
axs[2, 1].plot(time, broad, 'b-', label='Broad Money Data')
axs[2, 1].plot(time, broad_trend, 'r--', label='Broad Money Trend')
axs[2, 1].set_title('Broad Money Trend vs Data')
axs[2, 1].set_ylabel('Broad Money')
axs[2, 1].set_xlabel('Time')
axs[2, 1].legend(loc='upper left')
axs[2, 1].grid(True, which='both', linestyle='--', alpha=0.7)
fig.tight_layout()
plt.show()

# Construct a plot with several subplots for the cyclical components
fig, axs = plt.subplots(3, 2, figsize=(12, 10), sharex=True)

# Plot GDP Cycle
axs[0, 0].plot(time, gdp_cycle, 'r--', label='GDP Cycle')
axs[0, 0].set_title('GDP Cycle')
axs[0, 0].set_ylabel('Real GDP')
axs[0, 0].legend(loc='upper left')
axs[0, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Real Consumption Cycle
axs[0, 1].plot(time, rcons_cycle, 'r--', label='Real Consumption Cycle')
axs[0, 1].set_title('Consumption Cycle')
axs[0, 1].set_ylabel('Consumption')
axs[0, 1].legend(loc='upper left')
axs[0, 1].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Investment Cycle
axs[1, 0].plot(time, inv_cycle, 'r--', label='Investment Cycle')
axs[1, 0].set_title('Investment Cycle')
axs[1, 0].set_ylabel('Investment')
axs[1, 0].legend(loc='upper left')
axs[1, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Unemployment Cycle
axs[1, 1].plot(time, unem_cycle, 'r--', label='Unemployment Cycle')
axs[1, 1].set_title('Unemployment Cycle')
axs[1, 1].set_ylabel('Unemployment')
axs[1, 1].legend(loc='upper left')
axs[1, 1].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Narrow Money Cycle
axs[2, 0].plot(time, narrow_cycle, 'r--', label='Narrow Money Cycle')
axs[2, 0].set_title('Narrow Money Cycle')
axs[2, 0].set_ylabel('Narrow Money')
axs[2, 0].set_xlabel('Time')
axs[2, 0].legend(loc='upper left')
axs[2, 0].grid(True, which='both', linestyle='--', alpha=0.7)

# Plot Broad Money Cycle
axs[2, 1].plot(time, broad_cycle, 'r--', label='Broad Money Cycle')
axs[2, 1].set_title('Broad Money Cycle')
axs[2, 1].set_ylabel('Broad Money')
axs[2, 1].set_xlabel('Time')
axs[2, 1].legend(loc='upper left')
axs[2, 1].grid(True, which='both', linestyle='--', alpha=0.7)
fig.tight_layout()
plt.show()

#  Construct ONE plot with the cyclical components to show the comovements with output etc
plt.figure()
plt.plot(time, gdp_cycle, label='GDP')
plt.plot(time, rcons_cycle, label='Consumption')
plt.plot(time, inv_cycle, label='Investment')
plt.plot(time, unem_cycle, label='Unemployment')
plt.xlabel('Time')
plt.ylabel('Cycle')
plt.title('UK: Cycle of Key Macroeconomic Variables')
plt.legend()
plt.axhline(y=0, color='red', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

plt.figure()
plt.plot(time, gdp_cycle, label='GDP')
plt.plot(time, narrow_cycle, label='Narrow Money')
plt.plot(time, broad_cycle, label='Broad Money')
plt.xlabel('Time')
plt.ylabel('Cycle')
plt.title('UK: Cycle of Key Macroeconomic Variables (Monetary)')
plt.legend()
plt.axhline(y=0, color='red', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.show()

# Regarding fiscal variables plot two key fiscal metrics: Public debt to GDP and public deficit to GDP
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, debt_to_gdp, label='Debt to GDP')
plt.xlabel('Time')
plt.ylabel('Debt (% of GDP)')
plt.title('UK: Debt and Deficit as a Share of GDP')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(time, def_to_gdp, label='Deficit to GDP')
plt.xlabel('Time')
plt.ylabel('Deficit (% of GDP)')
plt.legend()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#Regarding zeta parameter: plot inflation, output growth rate and nominal interest rates and public debt of GDP in a plot with four subplots.
plt.figure(figsize=(10, 12))  # Increased figure size for clarity

plt.subplot(4, 1, 1)
plt.plot(time, public_debt, label='Public Debt', color='b')
plt.title('Public Debt Over Time')
plt.xlabel('Time')
plt.ylabel('Public Debt Levels')
plt.legend(loc='upper left')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(time_for_growth, inflation, label='Inflation', color='g')
plt.title('Inflation Over Time')
plt.xlabel('Time')
plt.ylabel('Inflation (%)')
plt.legend(loc='upper left')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(time_for_growth, rgdp_growth, label='Real GDP Growth', color='r')
plt.title('Real GDP Growth Rate Over Time')
plt.xlabel('Time')
plt.ylabel('GDP Growth Rate (%)')
plt.legend(loc='upper left')
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(time, stir, label='Short-Term Interest Rates', color='m')
plt.title('Short-Term Interest Rates Over Time')
plt.xlabel('Time')
plt.ylabel('Interest Rate (%)')
plt.legend(loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()


###Subperiod analysis

##

# Google Sheets file ID extracted from the link
file_id = '1fl127IBQ6wGCB3H38Fdj_crQfy6OYfdm'

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file as an Excel file
output = 'subperiod_data.xlsx'
gdown.download(url, output, quiet=False)

# Load the Excel file
dat_sub = pd.read_excel(output)

# Extract data
time1 = dat_sub['time1']
gdp1 = dat_sub['REAL_GDP 1']
gdp1_cycle, gdp1_trend = hpfilter(gdp1, lamb=100)
cons1 = dat_sub['REAL_CONS 1']
cons1_cycle, cons1_trend = hpfilter(cons1, lamb=100)
inv_gdp1 = dat_sub['Investment to GDP Ratio 1']




inv1 = inv_gdp1 * gdp1
inv1_cycle, inv1_trend = hpfilter(inv1, lamb=100)
unem1 = dat_sub['Unemployment1']
unem1_cycle, unem1_trend = hpfilter(unem1, lamb=100)
narr1 = dat_sub['narrow1']
narr1_cycle, narr1_trend = hpfilter(narr1, lamb=100)
br1 = dat_sub['broad1']
brd1_cycle, brd1_trend = hpfilter(br1, lamb=100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time1, gdp1_cycle, label='gdp')
plt.plot(time1, cons1_cycle, label='consumption')
plt.plot(time1, inv1_cycle, label='investment')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend(loc='lower left')
plt.title('UK: Cyclical Components of the Variables (1870-1920)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(time1, gdp1_cycle, label='gdp')
plt.plot(time1, narr1_cycle, label='narrow')
plt.plot(time1, brd1_cycle, label='broad')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend()
plt.tight_layout()
plt.grid()
time2 = dat_sub['time2']
gdp2 = dat_sub['REAL_GDP 2']
gdp2_cycle, gdp2_trend = hpfilter(gdp2, lamb=100)
cons2 = dat_sub['REAL_CONS 2']
cons2_cycle, cons2_trend = hpfilter(cons2, lamb=100)
inv_gdp2 = dat_sub['Investment to GDP Ratio 2']
inv2 = inv_gdp2 * gdp2
inv2_cycle, inv2_trend = hpfilter(inv2, lamb=100)
unem2 = dat_sub['Unemployment2']
unem2_cycle, unem2_trend = hpfilter(unem2, lamb=100)
narr2 = dat_sub['narrow2']
narr2_cycle, narr2_trend = hpfilter(narr2, lamb=100)
br2 = dat_sub['broad2']
brd2_cycle, brd2_trend = hpfilter(br2, lamb=100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time2, gdp2_cycle, label='gdp')
plt.plot(time2, cons2_cycle, label='consumption')
plt.plot(time2, inv2_cycle, label='investment')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend(loc='lower left')
plt.title('UK: Cyclical Components of the Variables (1921-1970)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time2, gdp2_cycle, label='gdp')
plt.plot(time2, narr2_cycle, label='narrow')
plt.plot(time2, brd2_cycle, label='broad')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend()
plt.tight_layout()
plt.grid()

time3 = dat_sub['time3']
gdp3 = dat_sub['REAL_GDP 3']
gdp3_cycle, gdp3_trend = hpfilter(gdp3, lamb=100)
cons3 = dat_sub['REAL_CONS 3']
cons3_cycle, cons3_trend = hpfilter(cons3, lamb=100)
inv_gdp3 = dat_sub['Investment to GDP Ratio 3']
inv3 = inv_gdp3 * gdp3
inv3_cycle, inv3_trend = hpfilter(inv3, lamb=100)
unem3 = dat_sub['Unemployment3']
unem3_cycle, unem3_trend = hpfilter(unem3, lamb=100)
narr3 = dat_sub['narrow3']
narr3_cycle, narr3_trend = hpfilter(narr3, lamb=100)
br3 = dat_sub['broad3']
brd3_cycle, brd3_trend = hpfilter(br3, lamb=100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time3, gdp3_cycle, label='gdp')
plt.plot(time3, cons3_cycle, label='consumption')
plt.plot(time3, inv3_cycle, label='investment')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend(loc='lower left')
plt.title('UK: Cyclical Components of the Variables (1971-2020)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time3, gdp3_cycle, label='gdp')
plt.plot(time3, narr3_cycle, label='narrow')
plt.plot(time3, brd3_cycle, label='broad')
plt.xlabel('time')
plt.ylabel('Cyclical Components')
plt.legend()
plt.tight_layout()
plt.grid()

###Plotting only the monetary cycles so that I can see the plots
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time1, narr1, label='Data')
plt.plot(time1, narr1_cycle, label='Cycle')
plt.plot(time1, narr1_trend, label='Trend')
plt.legend()
plt.title('Narrow Money in the first period (1870-1920)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time1, br1, label='Data')
plt.plot(time1, brd1_cycle, label='Cycle')
plt.plot(time1, brd1_trend, label='Trend')
plt.legend()
plt.title('Broad Money in the first period (1870-1920)')
plt.grid()

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time2, narr2, label='Data')
plt.plot(time2, narr2_cycle, label='Cycle')
plt.plot(time2, narr2_trend, label='Trend')
plt.legend()
plt.title('Narrow Money in the second period (1921-1970)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time2, br2, label='Data')
plt.plot(time2, brd2_cycle, label='Cycle')
plt.plot(time2, brd2_trend, label='Trend')
plt.legend()
plt.title('Broad Money in the second period (1921-1970)')
plt.grid()
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time3, narr3, label='Data')
plt.plot(time3, narr3_cycle, label='Cycle')
plt.plot(time3, narr3_trend, label='Trend')
plt.legend()
plt.title('Narrow Money in the third period (1971-2020)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time3, br3, label='Data')
plt.plot(time3, brd3_cycle, label='Cycle')
plt.plot(time3, brd3_trend, label='Trend')
plt.legend()
plt.title('Broad Money in the third period (1971-2020)')
plt.grid()
plt.tight_layout() 

###Subperiod analysis for the zeta parameter
###using the same time variables
interest1=dat_sub['interest1']
cpi1=dat_sub['cpi1']
interest2=dat_sub['interest2']
cpi2=dat_sub['cpi2']
interest3=dat_sub['interest3']
cpi3=dat_sub['cpi3']

inflation1 = [] 
for i in range(1, len(time1)):
    b = (cpi1[i] - cpi1[i - 1]) / cpi1[i]
    inflation1.append(b)


rgdp_growth1 = []
for i in range(1, len(time1)):
    b = (gdp1[i] - gdp1[i - 1]) / gdp1[i]
    rgdp_growth1.append(b)
del(interest1[0])

debt1=[]
for i in range(0,len(time1)):
    b=debt_to_gdp[i]
    debt1.append(b)
interest1 = interest1 + 1  
rgdp_growth1 = np.array(rgdp_growth1)  
inflation1 = np.array(inflation1)  
zeta1 = (1 + interest1) / ((1 + rgdp_growth1) + (1 + inflation1))


##Plotting the debt of the first period 
time1_growth=[]
for i in range(1,len(time1)):
    b=time1[i]
    time1_growth.append(b)
plt.figure()
plt.subplot(5,1,1)
plt.plot(time1_growth,zeta1,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta')
plt.title('UK:Zeta Parameter and Debt  from 1870 to 1920')
plt.legend()
plt.grid()

plt.subplot(5,1,2)
plt.plot(time1_growth ,interest1,label='Interest')
plt.xlabel('time')
plt.ylabel('measures')
plt.legend()
plt.grid()

plt.subplot(5,1,3)
plt.plot(time1_growth,rgdp_growth1,label='GDP')
plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()

plt.subplot(5,1,4)
plt.plot(time1_growth,inflation1,label='Inflation')
plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()

plt.subplot(5,1,5)
plt.plot(time1,debt_abs[0:50],label='Debt to GDP')
plt.xlabel('time')
plt.ylabel('Debt (%of GDP)')
plt.legend()
plt.grid()

##for second period
interest2 = dat_sub['interest2']
cpi2 = dat_sub['cpi2']

inflation2 = [] 
for i in range(1,len(time2)):
    b = (cpi2[i] - cpi2[i - 1]) / cpi2[i]
    inflation2.append(b)

rgdp_growth2 = []
for i in range(1, len(time2)):
    b = (gdp2[i] - gdp2[i - 1]) / gdp2[i]
    rgdp_growth2.append(b)

del(interest2[0])



interest2 = interest2 + 1  
rgdp_growth2 = np.array(rgdp_growth2)  
inflation2 = np.array(inflation2)  
zeta2 = (1 + interest2) / ((1 + rgdp_growth2) + (1 + inflation2))

time2_growth=[]
for i in range(1,50):
    b=time2[i]
    time2_growth.append(b)

plt.figure()
plt.subplot(5,1,1)
plt.plot(time2_growth,zeta2,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta')
plt.title('UK:Zeta Parameter and Debt from 1921 to 1970')
plt.legend()
plt.grid()
plt.subplot(5,1,2)
plt.plot(time2_growth ,interest2,label='Interest')
plt.xlabel('time')
plt.ylabel('measures')
plt.legend()
plt.grid()

plt.subplot(5,1,3)
plt.plot(time2_growth,rgdp_growth2,label='GDP')
plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()

plt.subplot(5,1,4)
plt.plot(time2_growth,inflation2,label='Inflation')
plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()

plt.subplot(5,1,5)
plt.plot(time2,debt_abs[50:100],label='Debt to GDP')
plt.xlabel('time')
plt.ylabel('Debt (%of GDP)')
plt.legend()
plt.grid()

interest3 = dat_sub['interest3']
cpi3 = dat_sub['cpi3']

inflation3 = [] 
for i in range(1,len(time3)):
    b = (cpi3[i] - cpi3[i - 1]) / cpi3[i]
    inflation3.append(b)

rgdp_growth3 = []
for i in range(1, len(time3)):
    b = (gdp3[i] - gdp3[i - 1]) / gdp3[i]
    rgdp_growth3.append(b)

del(interest3[0])



interest3 = interest2 + 1  
rgdp_growth3 = np.array(rgdp_growth2)  
inflation3 = np.array(inflation3)  
zeta3 = (1 + interest3) / ((1 + rgdp_growth3) + (1 + inflation3))

time3_growth=[]
for i in range(1,50):
    b=time3[i]
    time3_growth.append(b)

plt.figure()
plt.subplot(5,1,1)
plt.plot(time3_growth,zeta3,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta')
plt.title('UK:Zeta Parameter and Debt from 1971 to 2020')
plt.legend()
plt.grid()
plt.subplot(5,1,2)
plt.plot(time3_growth ,interest3,label='Interest')
plt.xlabel('time')
plt.ylabel('measures')
plt.legend()
plt.grid()

plt.subplot(5,1,3)
plt.plot(time3_growth,rgdp_growth3,label='GDP')
plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()

plt.subplot(5,1,4)
plt.plot(time3_growth,inflation3,label='Inflation')    

plt.xlabel('time')
plt.ylabel('Measures')
plt.legend()
plt.grid()
plt.subplot(5,1,5)
plt.plot(time3,debt_abs[101:151],label='Debt to GDP')
plt.xlabel('time')
plt.ylabel('Debt (%of GDP)')     
plt.legend()
plt.grid()


######Zeta parameter from 1870 to 1920

plt.figure()
plt.plot(time1_growth,zeta1,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta Parameter')
plt.title('Zeta Parameter (period1)')
plt.grid()
plt.legend()


plt.figure()
plt.subplot(3,1,1)
plt.plot(time1_growth,interest1,label='Interest Payments')
plt.xlabel('time')
plt.title('UK:zeta parameter decomposition (period1)')
plt.grid()
plt.legend()

plt.subplot(3,1,2)
plt.plot(time1_growth,rgdp_growth1,label='Real GDP growth')

plt.grid()
plt.legend()

plt.subplot(3,1,3)
plt.plot(time1_growth,inflation1,label='Inflation Rate')

plt.grid()
plt.legend()

######Zeta parameter from 1921-1970
plt.figure()
plt.plot(time2_growth,zeta2,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta Parameter')
plt.title('Zeta Parameter (period2)')
plt.grid()
plt.legend()


plt.figure()
plt.subplot(3,1,1)
plt.plot(time2_growth,interest2,label='Interest Payments')
plt.xlabel('time')

plt.title('UK:zeta parameter decomposition (period2)')
plt.grid()
plt.legend()

plt.subplot(3,1,2)
plt.plot(time2_growth,rgdp_growth2,label='Real GDP growth')

plt.grid()
plt.legend()

plt.subplot(3,1,3)
plt.plot(time2_growth,inflation2,label='Inflation Rate')

plt.grid()
plt.legend()



######Zeta parameter from 1971-2020
plt.figure()
plt.plot(time3_growth,zeta3,label='Zeta Parameter')
plt.xlabel('time')
plt.ylabel('Zeta Parameter')
plt.title('Zeta Parameter (period3)')
plt.grid()
plt.legend()


plt.figure()
plt.subplot(3,1,1)
plt.plot(time3_growth,interest3,label='Interest Payments')
plt.xlabel('time')

plt.title('UK:zeta parameter decomposition (period3)')
plt.grid()
plt.legend()

plt.subplot(3,1,2)
plt.plot(time3_growth,rgdp_growth3,label='Real GDP growth')

plt.grid()
plt.legend()

plt.subplot(3,1,3)
plt.plot(time3_growth,inflation3,label='Inflation Rate')

plt.grid()
plt.legend()



