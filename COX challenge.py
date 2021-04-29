#!/usr/bin/env python
# coding: utf-8


#COO Challenge
# In[7]:

import pandas as pd
csv6 = pd.read_csv("data/006_lomo_orders_dataset.csv")
csv6.head(3)
csv6.count()

# In[4]:

import pandas as pd
csv7 = pd.read_csv("data/007_lomo_order_items_dataset.csv")
csv7.head(3)
# In[30]:

import pandas as pd
csv4 = pd.read_csv("data/004_lomo_products_dataset.csv")
csv4.head(3)
csv4.count()

# In[5]:

merged_67 = csv6.merge(csv7,on=["order_id"])
merged_67.head(3)

# In[28]:
grouped = merged_67.groupby(['order_status'] , sort = False).count()

# In[29]:
grouped
# In[31]:
merged_674 = merged_67.merge(csv4,on=["product_id"])
merged_674.head(3)
# In[32]:
merged_674.count()
# In[50]:

merged_674.to_csv('merged_674_.csv', index =False)

# In[39]:
csv5 = pd.read_csv("data/005_lomo_product_category_name_translation.csv")
csv5.head(3)
# In[44]:
csv_5 = csv5.rename(columns = {'product_category_name_portugese':'product_category_name'})
csv_5

# In[46]:
merged_6745 = merged_674.merge(csv_5,on=["product_category_name"])
# In[48]:
merged_6745.to_csv('merged_6745_.csv', index =False)

# In[51]:
csv10 = pd.read_csv("data/010_lomo_marketing_qualified_leads_dataset.csv")
csv10.head(3)
csv10.count()
csv11 = pd.read_csv("data/011_lomo_closed_deals_dataset.csv")
csv11.head(3)
csv11.count()

# In[53]:

merged_leads = csv10.merge(csv11,on=["mql_id"])

# In[54]:

merged_leads.to_csv('merged_leads.csv', index =False)

#CFO Challenge
csv9 = pd.read_csv("data/009_lomo_order_reviews_dataset.csv")
csv9.head(3)
csv79 = merged_6745
csv79.head(2)
csv79 = csv79.merge(csv9,on=["order_id"])
csv79.head(3)   
csv79.to_csv('merged_79.csv', index =False)
csv79.drop(columns=['order_purchase_timestamp','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date'])
csv79.to_csv('merged_79_updated.csv', index =False)
grouped_nw = Networkdf.groupby(['product_category_name_english'] , sort = False).count()




