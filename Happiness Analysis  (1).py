#!/usr/bin/env python
# coding: utf-8

# ## IMPORTING RAW DATA FROM EXCEL USING PANDAS

# In[93]:


import pandas as pd

WHR_df=pd.read_excel("C:\\Users\\aditi\OneDrive\Desktop\Project\DataPanelWHR2021C2.xls")

print(WHR_df.head(10))


# ## FILTERING COUNTRIES EACH HAVING 5 YEARS OF DATA FROM 2016-2020 USING IMPORTED DATA FROM EXCEL

# In[94]:


#Filter Original DataFrame For Data Between 2016-2020( 5 years)
WHR_16_20=WHR_df[(WHR_df['year']==2016) | (WHR_df['year']==2017) | (WHR_df['year']==2018) | (WHR_df['year']==2019) | (WHR_df['year']==2020)]
print('DATAFRAME CONTAINING DATA FROM 2017-2020')
print(WHR_16_20)
print('                      ')

#Count Of Years In Each Country In DataFrame Above
YearCountInCountry=WHR_16_20.groupby(by=['Country name'])['year'].count()
print('COUNTRIES LIST WITH COUNT OF YEARS IN EACH COUNTRY FOR DATA FROM 2016-2020 :')
print(YearCountInCountry)
print('                      ')

#Select Countries With Count Of Five Years
CountriesWithFiveYears=YearCountInCountry[YearCountInCountry==5]
print('COUNTRIES LIST WITH COUNT OF FIVE YEARS IN EACH COUNTRY FOR DATA FROM 2016-2020:')
print(CountriesWithFiveYears)
print('                      ')

#Setting Index to Country name
WHR_16_20=WHR_16_20.set_index(['Country name'])
print('DATAFRAME WITH DATA FROM 2016-2020 & INDEX AS COUNTRY NAME:')
print(WHR_16_20)
print('                      ')

#DataFrame Containing Data For Five Years For Each Country
WHRfive_16_20=WHR_16_20[WHR_16_20.index.isin(CountriesWithFiveYears.index)]
print('DATAFRAME CONTAINING DATA FOR FOUR YEARS FROM 2017-2020 FOR EACH COUNTRY:')
print(WHRfive_16_20)
print('                      ')



# ## COUNT OF COUNTRIES, EACH CONTAINING DATA FOR FIVE YEARS(2016-2020)

# In[95]:


#Count Of Countries Containing Data For Five Years
WHRfive_16_20=WHRfive_16_20.reset_index()
CountOfCountries_WHRfive_16_20=WHRfive_16_20['Country name'].nunique()
print('COUNT OF COUNTRIES CONTAINING DATA FROM 2016-2020:')
print(CountOfCountries_WHRfive_16_20)
print('                      ')


# # 2016-2019 ANALYSIS(Pre-Covid)

# ## 1. Average Life Ladder From 2016-2019

# In[96]:


#Filter Data Between 2016-2019 From DataFrame (2016-2020)
WHR_16_19=WHRfive_16_20[((WHRfive_16_20['year']==2016) | (WHRfive_16_20['year']==2017) | (WHRfive_16_20['year']==2018) | 
                        (WHRfive_16_20['year']==2019)) & (WHRfive_16_20['Life Ladder']!=' ')]

AverageLifeLadder=WHR_16_19['Life Ladder'].mean()
AverageLifeLadder.round(2)


# ## 2.Top 5 & Bottom 5 Countries By Average Of Life Ladder From 2016-2019

# In[97]:


TopCountriesByAverageOfLifeLadder=WHR_16_19.groupby(by=['Country name'])['Life Ladder'].mean().sort_values(ascending=False)
Top5CountriesByAverageOfLifeLadder=TopCountriesByAverageOfLifeLadder.reset_index().head(5)

x=Top5CountriesByAverageOfLifeLadder

import matplotlib.pyplot as plt

plt.plot(x['Country name'], x['Life Ladder'])
plt.title("Top5CountriesByAverageOfLifeLadder")
plt.xlabel("Country name")
plt.ylabel("Life Ladder")
plt.show()

Bottom5CountriesByAverageOfLifeLadder=TopCountriesByAverageOfLifeLadder.reset_index().tail(5)
y=Bottom5CountriesByAverageOfLifeLadder

plt.plot(y['Country name'], y['Life Ladder'])
plt.title("Bottom5CountriesByAverageOfLifeLadder")
plt.xlabel("Country name")
plt.ylabel("Life Ladder")
plt.show()



# ## 3. Effect & Correlation On Average Life Ladder & Average Healthy Life-Expectancy By Log GDP Per Capita(2016-2019)

# In[228]:


#Filtering Data According To Each Of 3 Metrics & Avearging Each Of Them
AvgHealthLifeExpectancy=WHR_16_19.groupby(by=['Country name'])['Healthy life expectancy at birth'].mean().sort_values()
AvgLifeLadder=WHR_16_19.groupby(by=['Country name'])['Life Ladder'].mean().sort_values()
AvgLog=WHR_16_19.groupby(by=['Country name'])['Log GDP per capita'].mean().sort_values()

#Line Plot Specifications
x=AvgLog
y1=AvgHealthLifeExpectancy
y2=AvgLifeLadder

fig,ax1=plt.subplots()

ax2=ax1.twinx()

#Plotting the Graph
curve1=ax1.plot(AvgLog, y1, label='AvgHealthLifeExpectancy', color='r')
curve1=ax2.plot(AvgLog, y2, label='AvgLifeLadder', color='b')

plt.title("Effect on Avg. Life Ladder & Avg. Healthy Life Expectancy by Log GDP")
plt.plot()
plt.show()

#DataFrame Containing Average Metrics Of Four Years From 2016-2019 For Each Country
AverageMetrics_16_19=WHR_16_19.groupby(by=['Country name'])['Life Ladder','Log GDP per capita','Social support', 
                                                            'Healthy life expectancy at birth' , 'Freedom to make life choices', 
                                                            'Generosity','Perceptions of corruption', 'Positive affect', 
                                                            'Negative affect'].mean()
#Correlation Between Log GDP per capita & Life Ladder
print('CORRELATION BETWEEN Log GDP per capita & Life Ladder')
print(AverageMetrics_16_19['Log GDP per capita'].corr(AverageMetrics_16_19['Life Ladder']))

#Correlation Between Log GDP per capita & Healthy life expectancy at birth
print('CORRELATION BETWEEN Log GDP per capita & Healthy life expectancy at birth')
print(AverageMetrics_16_19['Log GDP per capita'].corr(AverageMetrics_16_19['Healthy life expectancy at birth']))


# ## 4. Correlation & Effect On Average Life Ladder By Average Freedom To Make Life Choices & Average Social Support(2016-2019)

# In[231]:


#Filtering Data According To Each Of 3 Metrics and avearging each of them
AvgLifeLadder=WHR_16_19.groupby(by=['Country name'])['Life Ladder'].mean().sort_values()
AvgFreedom=WHR_16_19.groupby(by=['Country name'])['Freedom to make life choices'].mean().sort_values()
AvgSocialSupport=WHR_16_19.groupby(by=['Country name'])['Social support'].mean().sort_values()

#Declaring subplot specification
fig, ax = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 2]})
fig.tight_layout()

#subplot1
plt.subplot(1,2,1)
plt.plot(AvgFreedom,AvgLifeLadder)
plt.title("Effect on Avg.Life Ladder By Avg.Freedom")
plt.xlabel("Average Freedom")
plt.ylabel("Average Life Ladder")
fig.tight_layout()

#subplot2(
plt.subplot(1,2,2)
plt.plot(AvgSocialSupport,AvgLifeLadder)
plt.title("Effect on Avg.Life Ladder By Avg.Social Support")
plt.xlabel("Average Social Support")
plt.ylabel("Average Life Ladder")
fig.tight_layout()

#Correlation Between Freedom To Make Life Choices & Life Ladder
print('CORRELATION BETWEEN Freedom to make life choices & Life Ladder')
print(AverageMetrics_16_19['Freedom to make life choices'].corr(AverageMetrics_16_19['Life Ladder']))

#Correlation Between Social Support & Life Ladder
print('CORRELATION BETWEEN Social Support & Life Ladder')
print(AverageMetrics_16_19['Social support'].corr(AverageMetrics_16_19['Life Ladder']))


# ## 5. Correlation & Effect On Average Positive Affect & Average Negative Affect By Average Life Ladder(2016-2019)

# In[235]:


#Filtering Data According To Each Of 3 Metrics And Avearging Each Of Them
AvgPositiveAffect=WHR_16_19.groupby(by=['Country name'])['Positive affect'].mean().sort_values()
AvgNegativeAffect=WHR_16_19.groupby(by=['Country name'])['Negative affect'].mean().sort_values()
AvgLifeLadder=WHR_16_19.groupby(by=['Country name'])['Life Ladder'].mean().sort_values()

#Declaring plot specification
x=AvgLifeLadder
y1=AvgPositiveAffect
y2=AvgNegativeAffect
fig,ax1=plt.subplots()
ax2=ax1.twinx()

#Plotting the Graph-RedLine-Positive, BlueLine-Negative
curve1=ax1.plot(x, y1, label='AvgPositiveAffect', color='r')
curve1=ax2.plot(x, y2, label='AvgNegativeAffect', color='b')
plt.title("Effect on Avg.Positive Affect & Avg.Negative Affect By Avg.Life Ladder")
plt.xlabel("Life Ladder")
plt.plot()
plt.show()
fig.tight_layout()

#Correlation Between Positive Affect & Life Ladder
print('CORRELATION BETWEEN Positive Affect & Life Ladder')
print(AverageMetrics_16_19['Positive affect'].corr(AverageMetrics_16_19['Life Ladder']))

#Correlation Between Negative Affect & Life Ladder
print('CORRELATION BETWEEN Negative Affect & Life Ladder')
print(AverageMetrics_16_19['Negative affect'].corr(AverageMetrics_16_19['Life Ladder']))


# ## 6. Other Correlations Between Metrics(2016-2029)

# In[ ]:


print('CORRELATION BETWEEN Freedom to make life choices & Positve affect')
print(AverageMetrics_16_19['Freedom to make life choices'].corr(AverageMetrics_16_19['Positive affect']))

print('CORRELATION BETWEEN Generosity & Positve affect')
print(AverageMetrics_17_19['Generosity'].corr(AverageMetrics_17_19['Positive affect']))

print('CORRELATION BETWEEN Social support & Positve affect')
print(AverageMetrics_17_19['Social support'].corr(AverageMetrics_17_19['Positive affect']))

print('CORRELATION BETWEEN Healthy life expectancy at birth & Positve affect')
print(AverageMetrics_17_19['Healthy life expectancy at birth'].corr(AverageMetrics_17_19['Positive affect']))

print('CORRELATION BETWEEN Log GDP per capita & Positve affect')
print(AverageMetrics_17_19['Log GDP per capita'].corr(AverageMetrics_17_19['Positive affect']))

print('CORRELATION BETWEEN Perceptions of corruption & Positve affect')
print(AverageMetrics_17_19['Perceptions of corruption'].corr(AverageMetrics_17_19['Positive affect']))



# # ANALYSIS FROM 2019-2020(Transitioning To Covid)

# ## 1. Top 5 Countries By Taking Average of Life Ladder in (2019-2020)

# In[224]:


#Filter Data For 2019-2020 From DataFrame 2016-2020(WHRfive_16_20) Without Null Values in Life Ladder
WHR_19_20=WHRfive_16_20[((WHRfive_16_20['year']==2019) | (WHRfive_16_20['year']==2020)) & (WHRfive_16_20['Life Ladder']!=' ')]

#Finding Average of Life Ladder & Sorting Filtered Data According To Life Ladder In Descending Order
Top5CountriesByAvgLifeLadder_19_20=WHR_19_20.groupby(by=['Country name'])['Life Ladder'].mean().sort_values(ascending=False)

#Filtering Top 5 Countries
x=Top5CountriesByAvgLifeLadder_19_20.reset_index().head(5)

#Plotting Line Graph
plt.plot(x['Country name'],x['Life Ladder'])


# ## 2. Top 5 Countries By Increase In Average Of Life Ladder From  2019 To 2020

# In[227]:


#Filter Data For 2019 From DataFrame 2016-2020(WHRfive_16_20) Without Null Values in Life Ladder
WHR_19=WHRfive_16_20[((WHRfive_16_20['year']==2019)) & (WHRfive_16_20['Life Ladder']!=' ')].sort_values(by=['Country name'])

#Changing Index To Country Name(to keep only numeric Data in Columns) in DataFrame For 2019(WHR_19)
x=WHR_19.set_index('Country name')

#Filter Data For 2020 From DataFrame 2016-2020(WHRfive_16_20) Without Null Values in Life Ladder
WHR_20=WHRfive_16_20[((WHRfive_16_20['year']==2020)) & (WHRfive_16_20['Life Ladder']!=' ')].sort_values(by=['Country name'])

#Changing Index To Country Name(to keep only numeric Data in Columns) in DataFrame For 2020(WHR_20)
y=WHR_20.set_index('Country name')

#Finding Difference Between Average Life Ladder From 2019 to 2020
diff=y['Life Ladder']-x['Life Ladder']

#Finding Increase Between Average Life Ladder From 2019 to 2020(by keeping (diff>0))
#Filtering Top 5 Countries By Sorting Life Ladder in Descending order
Top5CountriesWithIncFrom19_20=((diff[diff>0]).sort_values(ascending=False).head(5))
Top5CountriesWithIncFrom19_20


# ## 3. Contributing Factors For Increase In Life Ladder For Top 5 Countries B/w 2019 To 2020 (shown as percentage)(2019-2020)

# In[185]:


ChangePerc=((y-x)/x)*100
Factors=ChangePerc[ChangePerc.index.isin(Top5CountriesWithIncFrom19_20.index)]
Factors=Factors.sort_values(by=['Life Ladder'], ascending=False)
Factors


# ## 4. Top 5 Countries By Decrease In Life Ladder From 2019 To 2020

# In[182]:


dec=x['Life Ladder']-y['Life Ladder']

Top5CountriesWithDecFrom19_20=((dec[dec>0]).sort_values(ascending=False).head(5))

Top5CountriesWithDecFrom19_20


# ## 5. Contributing Factors For Decrease In Life Ladder For Top 5 Countries B/w 2019 To 2020 (shown as percentage)(2019-2020)

# In[193]:


DecPerc=((x-y)/x)*100
Factors_DecPerc=DecPerc[DecPerc.index.isin(Top5CountriesWithDecFrom19_20.index)]
Factors_DecPerc=Factors_DecPerc.sort_values(by=['Life Ladder'], ascending=False)
Factors_DecPerc.drop( ['Life Ladder', 'year'],axis=1, inplace=True)
Factors


# 
# # 2017 ANALYSIS

# ## 1. Filter Data For 2017 

# In[223]:


#Filter Data For Year 2017 Without Null(Positive affect) Values
WHRfive_17=WHRfive_16_20[(WHR_df['year']==2017) & (WHR_df['Positive affect']!='NaN')]

WHRfive_17.head(5)


# ## 2. Total Countries Having Data For 2017 

# In[ ]:


#Total Countries Having Data For 2017
CountOfCountries_WHRfive_17=WHRfive_17['Country name'].nunique()
print('TOTAL COUNTRIES HAVING DATA FOR 2017:')
print(CountOfCountries_WHRfive_17)
print('                      ')


# ## 3. Top 5 Countries with Most positive Affect In 2017

# In[220]:


#Sorting Data According To Positive Affect In Descending
WHRfive_17_sort=WHRfive_17.sort_values(by=['Positive affect'], ascending=False)

#Top 5 Countries With Most Positive Affect
Top5CountriesWithPositiveAffect=WHRfive_17_sort.head(5)
print('TOP 5 COUNTRIES WITH MOST POSITIVE AFFECT:')
print(Top5CountriesWithPositiveAffect)
print('                      ')

#Creating Bar Graph For Top 5 Countries With Most Positive Affect
fig = plt.figure(figsize = (5, 3))
plt.bar(Top5CountriesWithPositiveAffect['Country name'], Top5CountriesWithPositiveAffect['Positive affect'], 
        color ='maroon', width = 0.4)
plt.xlabel("Country name")
plt.ylabel("Postive affect")
plt.title("Top 5 Countries With Most Positive Affect")
plt.show()


# ## 4. Bottom 5 Countries With Least Positive Affect In 2017

# In[221]:


#Bottom 5 Countries With Least Positive Affect 
Bottom5CountriesWithLeastPositiveAffect=WHRfive_17_sort.tail(5)
print('BOTTOM 5 COUNTRIES WITH LEAST POSITIVE AFFECT:')
print(Bottom5CountriesWithLeastPositiveAffect)
print('                      ')

#Creating Bar Graph For Bottom 5 Countries With Least Positive Affect 
fig = plt.figure(figsize = (5, 3))
plt.bar(Bottom5CountriesWithLeastPositiveAffect['Country name'], Bottom5CountriesWithLeastPositiveAffect['Positive affect'], 
        color ='green', width = 0.4)
plt.xlabel("Country name")
plt.ylabel("Postive affect")
plt.title("Bottom 5 Countries With Least Positive Affect")
plt.show()


# # FILTERING & COMPARING AVERAGE METRICS B/W PERIOD(2016-2019) & PERIOD 2020  
# 

# In[210]:


#Filtering DataFrame For Four Years(2016-2019) From DataFrame(2016-2020) 
WHR_16_19=WHRfive_16_20[(WHRfive_16_20['year']==2016) | (WHRfive_16_20['year']==2017) | (WHRfive_16_20['year']==2018) | 
                        (WHRfive_16_20['year']==2019)]

#DataFrame Containing Average Metrics Of Four Years From 2016-2019 For Each Country
AverageMetrics_16_19=WHR_16_19.groupby(by=['Country name'])['Life Ladder','Log GDP per capita','Social support', 
                                                            'Healthy life expectancy at birth' , 'Freedom to make life choices', 
                                                            'Generosity','Perceptions of corruption', 'Positive affect', 
                                                            'Negative affect'].mean()

AverageMetrics_16_19=AverageMetrics_16_19.sort_values(by=['Country name'])

#DataFrame Containing Data For 2020 For Each Country
Metrics_20=WHRfive_16_20[(WHRfive_16_20['year']==2020)]
Metrics_20= Metrics_20.groupby(by=['Country name'])['Life Ladder','Log GDP per capita','Social support', 
                                                            'Healthy life expectancy at birth' , 'Freedom to make life choices', 
                                                            'Generosity','Perceptions of corruption', 'Positive affect', 
                                                            'Negative affect'].mean()

Metrics_20=Metrics_20.sort_values(by=['Country name'])

#Difference In Metrics Between y2020 & From Period y2016-y2019
(Metrics_20-AverageMetrics_16_19).sort_values(by=['Life Ladder'],ascending=False).head(5)


# In[ ]:




