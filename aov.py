
#### Load required libraries
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

dataset = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")

dataset.isnull().sum()

dataset.describe()

dataset.info()

sns.boxplot(data=dataset.order_amount, orient="h").set_title('order amount')

sns.boxplot(data=dataset.total_items, orient="h").set_title('total item')


dataset['priceperitem'] = dataset['order_amount']/dataset['total_items']

dataset.describe()

z = dataset[dataset['total_items']>100]
print(z.shape)

sns.boxplot(data=dataset.priceperitem, orient="h").set_title('price per item')

#shop no 78 is the only shop which sells show at high rate
a = dataset[(dataset['priceperitem']>388) &( dataset['total_items'] < 10)]
print(a.shape)
print(a)

index = dataset[(dataset['priceperitem']>388)].index.values

df  = dataset.drop(index,axis=0).reset_index(drop=True)

df['order_amount'].describe()

dataset['priceperitem'].unique()

p112 = dataset[dataset['priceperitem'] == 112]

s7 = dataset[dataset['shop_id'] == 53]

df2 = dataset.groupby(['shop_id']).agg({'order_amount': ['mean','sum']})
df2.columns = ['mean','sum']

df2.describe()








