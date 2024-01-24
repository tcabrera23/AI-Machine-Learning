#!/usr/bin/env python
# coding: utf-8

# # Credit Approval Prediction

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"clean_dataset.csv")
df

# Documentar que hice la matriz de correlacion entre los datos categoricos y la correlacion era < |0.01|. Ese analisis servia mas para relacionar la etnicidad con la profesion y el trabajo de industria o si tenia que ver el ser ciudadano de nacimiento con la industria (capaz los que no, los extranjerpos, se dedican mas a otro tipo de area etc)
# ### Hago un analisis de mis datos

# In[36]:


df.hist(figsize=(10,8));


# ### Analizo la correlacion de mis variables

# In[37]:


import seaborn as sns

plt.figure(figsize=(16,12))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")


# In[38]:


# Voy a excluir de mi modelo algunas columnas que tienen muy bajo impacto en mi prediccion
df = df.drop(['Gender', 'DriversLicense',  'ZipCode', "Industry", "Ethnicity", "Citizen"], axis=1)
df.head()


# In[40]:


# Defino mis variables
response = df[['Approved']]
predictors = df.drop('Approved', axis=1)


# In[41]:


import seaborn as sns

plt.figure(figsize=(16,12))
sns.heatmap(predictors.corr(), annot=True, cmap="YlGnBu")


# In[42]:


# Cantidad de registros por variable independiente
for predictor in list(predictors):
    plt.hist(predictors[predictor])
    plt.title(predictor)
    plt.show()


# In[43]:


from sklearn.model_selection import train_test_split

split = train_test_split(predictors, response, test_size=0.3, random_state=99)

predictors_train = split[0]
predictors_test = split[1]
response_train = split[2]
response_test = split[3]

print(predictors.shape)
print(response.shape)
print()
print(predictors_train.shape)
print(predictors_test.shape)
print(response_train.shape)
print(response_test.shape)


# In[44]:


# Una vez que ya separé mis datos, debo decidir que modelo utilizar
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(max_depth=2)
classifier.fit(predictors_train, response_train)


# In[45]:


from sklearn.metrics import classification_report, confusion_matrix

response_predictions = classifier.predict(predictors_test)
print("  TN  FP")
print(confusion_matrix(response_test, response_predictions))
print("  FN  TP")
print()
print(classification_report(response_test, response_predictions,target_names=["No Approved","Approved"]))


# In[62]:


# El credit score suele darse en la franja de los 25 y 40 años y baja considerablemente despues de los 55
plt.scatter(df["Age"], df["CreditScore"])
plt.show()

