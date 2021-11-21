#!/usr/bin/env python
# coding: utf-8

# ## Appendix
# 
# - click on the links:
# 
# >1. <a href=#imports>imports</a> 
# >2. <a href=#load>Load Data </a>
# >3. <a href=#Formating>Data formating </a>
# >4. <a href=#Exp_uni_var>Exploratory Data Analysis(Uni-variable) </a>
# >5. <a href=#Exp_muli_var>Exploratory Data Analysis(muli-variable-RelationShips) </a>
# >6. <a href=#Q&insights>Questions & Insights </a>
# >7. <a href=#conclusion>Conclusion </a>

# ### <a name = 'imports'>imports</a>

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")
print ("[done]")


# ### <a name='load'>Load Data </a>

# In[3]:


df= pd.read_csv('Salary by Education.csv')# reading csv files
df


# In[4]:


ls


# ### <a name='Formating'>Data formating </a>

# In[5]:


df.info()


# In[6]:


df.head(5)


# In[37]:


df['Degree Level'].value_counts()


# In[38]:


df['Nationality'].value_counts()


# In[39]:


df['Gender'].value_counts()


# In[40]:


df['Degree Level'].nunique()


# In[41]:


df['Nationality'].nunique()


# In[42]:


df['Degree Level'].unique()


# In[43]:


df.drop('Currency',axis =1)


# ### <a name='Exp_uni_var'>Exploratory Data Analysis(Uni-variable) </a>

# In[33]:


sns.barplot(x='Nationality', y='Salary', data=dff, estimator=np.median)


# In[34]:


sns.barplot(x='Gender', y='Salary', data=df, estimator=np.mean)


# In[35]:


sns.barplot(x='Nationality', y='Salary', data=df, estimator=np.max)
#max salary for female and male(8)


# In[36]:


sns.barplot(x='Degree Level', y='Salary', data=df, estimator=np.mean)


# ### <a name='Exp_muli_var'>Exploratory Data Analysis(muli-variable-RelationShips) </a>

# In[9]:


fig = px.box(df,x="Year Quarter", y="Salary", color="Gender",title="Eraning more for Gender")
fig.show()


# # Who is earning more? Saudi or non Saudi 

# In[10]:


fig = px.box(df, x="Year Quarter", y="Salary", color="Nationality" ,title="Earning more for Nationality")
fig.show()


# In[12]:


fig = px.box(df, x="Year Quarter", y="Salary", color="Degree Level" ,title="Salary from 2017 -2021")
fig.show()


# ### who is eraning more?
# 1- male more than female on salary and employment rate 

# In[13]:


dff = df.groupby(['Year Quarter', 'Gender']).mean().reset_index()
fig = px.line(dff, x="Year Quarter", y="Salary",color='Gender',title="Mean Earnings for Gender")
fig.show()


# mean of earnings for Gender..

# In[14]:


dff = df.groupby(['Year Quarter', 'Nationality']).mean().reset_index()
fig = px.line(dff, x="Year Quarter", y="Salary",color='Nationality',title=" Mean of earnings for Nationality")
fig.show()


# In[15]:


df.groupby(['Year Quarter', 'Degree Level']).mean().reset_index()


# In[16]:


dff = df.groupby(['Year Quarter', 'Degree Level']).mean().reset_index()
fig = px.line(dff, x="Year Quarter", y="Salary",color='Degree Level',title="Salary from 2017 -2021 with Degree Level ")
fig.show()


# In[17]:


dff = df.groupby(['Year Quarter', 'Gender', 'Nationality', 'Degree Level']).mean().reset_index()
dff['Level']  = dff['Degree Level']
fig = px.line(dff, x="Year Quarter", y='Salary',color='Gender',title='Salary from 2017 -2021 by Nationality, Gender & Degree Level ', facet_row='Nationality',
              facet_col='Level' , facet_col_spacing = 0.04,
             category_orders = {'Level': ['Primary' ,'Secondary' , 'Intermediate' , 'Diploma' ,'Bachelor', 'Master Degree', 'Doctorate'],
                                               'Nationality': ['Saudi', 'NonSaudi'],
                                               'Gender': ['Male', 'Female']})
fig.show()


# In[19]:


whos


# In[24]:


df.describe()


# ### <a name ='Q&insights'>Questions & Insights </a>

# (3)#min and max salary for each level degree from 2017 -2021
# (8)#max salary for female and male
# (7)#min salary for saudi and non saudi
# (9)# Maen for saudi and non saudi

# ### <a name ='conclusion'>Conclusion </a>

# - Saudi have better sallary than non-Saudi regardless the level of education and gender.
# 
# - Male have better sallary than Female regardless the level of education and nationality.
# 
# - Linear regression model; Y= Sallary, X = Year, Gender, Nationality and level of education.
# 
# - Trend analysis using Joinpoint regression # Limitations.
# 
# - Sallary increases with advancement of education.
