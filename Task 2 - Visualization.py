#!/usr/bin/env python
# coding: utf-8

# # TASK 2 - Descriptive and Predictive analysis with interactive dashboard.

# In[ ]:





# In[2]:


#import libraries 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Create the dataset
data = {
    "Date": [
        "2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05",
        "2024-08-06", "2024-08-07", "2024-08-08", "2024-08-09", "2024-08-10"
    ],
    "Product": [
        "Product A", "Product B", "Product A", "Product C", "Product B",
        "Product A", "Product C", "Product B", "Product A", "Product C"
    ],
    "Region": [
        "North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South"
    ],
    "Sales": [100, 150, 200, 130, 170, 120, 180, 190, 210, 160]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display the DataFrame
print(df)


# In[ ]:





# #### Bar Chart - sale by product

# In[5]:


#bar chart
plt.figure(figsize=(4,4))
sns.barplot(x='Product', y='Sales',data=df, estimator=sum, ci=None)
plt.title("title sales by product")
plt.xlabel("product")
plt.ylabel("total sales")
plt.show()


# In[ ]:





# #### Line Chart - sales over time

# In[39]:


#line chart
plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="Sales", data=df, marker="o")
plt.title("sales over time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# In[ ]:





# #### Pie Chart - Sales Distribution By Region

# In[43]:


#calculate sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()

#Create a pie chart
plt.figure(figsize=(6,6))
plt.pie(sales_by_region, labels=sales_by_region.index, autopct='%1.1f%%', startangle=140)
plt.title("sales Distribution By Region")
plt.show()


# In[ ]:




