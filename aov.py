
#### Load required libraries
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

dataset = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")

dataset.isnull().sum()

dataset.describe()

dataset.info()

#box plot - order amount
sns.boxplot(data=dataset.order_amount, orient="h").set_title('order amount')

#box plot - total item
sns.boxplot(data=dataset.total_items, orient="h").set_title('total item')

#record with total items greater than mean (i.e) 8
totlitem = dataset[dataset['total_items']>8]
print(totlitem.shape)

#record with order anount greater than mean (i.e) 3145.13
ordeamount = dataset[dataset['order_amount']>3145.13]
print(ordeamount.shape)

#price of one shoe in each shop
dataset['priceperitem'] = dataset['order_amount']/dataset['total_items']

dataset.describe()

#record with price per shoe greater than mean (i.e) 387.74
ppitem = dataset[dataset['priceperitem']>387.74]
print(ppitem.shape)


#as we see ppitem record all the records are with shop_id = 78
#it is given that price of shoe is relatively affordable 
#But the shoe which is sold by shop 78 it is very high when compared to other shoes for other shops

#so i dropped all the data  from shop 78
final_data = dataset.drop(labels=dataset[dataset['shop_id']==78].index, axis=0)

final_data.describe()
final_data['order_amount'].describe()
#final aov - $2717.36









