#!/usr/bin/env python
# coding: utf-8

# # TASK 2 - Descriptive and Predictive analysis with interactive dashboard.

# In[ ]:





# In[1]:


#import libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


#sales data

Date = ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05",
        "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10"]

Product = ["Apple", "Banana", "Apple", "Cherry", "Banana",
        "Apple", "Cherry", "Banana", "Apple", "Cherry"]
    
Region = ["North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South"]

Sales = [100, 150, 200, 130, 170, 120, 180, 190, 210, 160]


# #### Bar Chart - sale by product

# In[49]:


#bar chart

data1 = np.array(Product)
data2 = np.array(Sales)

plt.bar(data1,data2)
plt.show()


# #### Line Chart - sales over time

# In[48]:


#line chart
data1 = np.array(Date)
data2 = np.array(Sales)

plt.figure(figsize=(14,4))
plt.plot(data1,data2)
plt.show()


# #### Pie Chart - Sales Distribution By Product

# In[52]:


#pie chart
data1 = np.array([10,20,30])
data2 = ["Apple", "Cherry", "Banana"]

plt.pie(data1,labels=data2)
plt.show()


# In[ ]:




