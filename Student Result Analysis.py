#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull.sum()


# In[5]:


df.isnull().sum()


# # Drop Unnamed Column

# In[6]:


df = df.drop("Unnamed: 0", axis=1)
df.head()


# # Gender Distribution

# In[7]:


plt.figure(figsize=(3,5))
ax = sns.countplot(data = df,x = 'Gender')
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# In[ ]:


#From the above chart we have analyzed that :-
#Analyzed that the number of female candiate is more than male


# In[8]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[9]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot=True)
plt.title("Parent Education VS Student Score")
plt.show()


# In[ ]:


#From the above chat we have concluded that education of the parents have a good impact on child education


# In[10]:


gb1= df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)


# In[11]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=True)
plt.title("Parent Marital Status VS Student Score")
print(gb1)


# In[ ]:


#From the above chart we have concluded that :-
#There is no/negligable on the student score due to theis parent's marital status


# In[12]:


gb2= df.groupby("WklyStudyHours").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb2)


# In[13]:


plt.figure(figsize=(4,4))
sns.heatmap(gb2,annot=True)
plt.title("Weekly Study Hours VS Student Score")
print(gb2)


# In[ ]:


#from the above chart we analyzed that:-
#Students who studied more than 10 hours a week have higher marks compared to others students 


# In[24]:


gb3= df.groupby("PracticeSport").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb3)


# In[23]:


plt.figure(figsize=(4,4))
sns.heatmap(gb3,annot=True)
plt.title("Practice Sports VS Student Score")
print(gb3)


# In[ ]:


#From the above chart we have analyzed that:-
#Practicing sports is also important for student's wellbeing and education


# In[15]:


plt.figure(figsize=(4,3))
sns.boxplot(data = df,x="MathScore")
plt.show()


# In[16]:


plt.figure(figsize=(4,3))
sns.boxplot(data = df,x="ReadingScore")
plt.show()


# In[22]:


plt.figure(figsize=(4,3))
sns.boxplot(data = df,x="WritingScore")
plt.show()


# In[ ]:


#from the above three visualization we noticed that:-
#Students are weak in maths compared to reading and writing


# In[20]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Group
# 

# In[27]:


GroupA = df.loc[(df['EthnicGroup'] == "group A")].count()
GroupB = df.loc[(df['EthnicGroup'] == "group B")].count()
GroupC = df.loc[(df['EthnicGroup'] == "group C")].count()
GroupD = df.loc[(df['EthnicGroup'] == "group D")].count()
GroupE = df.loc[(df['EthnicGroup'] == "group E")].count()



l=["group A","group B","group C","group D","group E"]
mlist=[GroupA["EthnicGroup"],GroupB["EthnicGroup"],GroupC["EthnicGroup"],GroupD["EthnicGroup"],GroupE["EthnicGroup"]]

print(mlist)
plt.pie(mlist, labels=l, autopct ="%1.2f%%")
plt.show()


# In[28]:


ax = sns.countplot(data= df,x ='EthnicGroup')
ax.bar_label(ax.containers[0])


# In[ ]:




