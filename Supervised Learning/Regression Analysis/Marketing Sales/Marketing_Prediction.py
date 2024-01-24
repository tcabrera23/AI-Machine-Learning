#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
marketing_dataset = pd.read_csv('marketing_data.csv')
print(marketing_dataset.head())
import numpy as np


# In[23]:


marketing_dataset.info()


# In[24]:


marketing_dataset["Influencer"].value_counts()


# In[25]:


marketing_dataset=pd.get_dummies(marketing_dataset,columns=["Influencer"])
marketing_dataset.head()


# In[26]:


marketing_dataset[marketing_dataset["Sales"] < 36].head(10)
# El motivo fue comparar el output de mi modelo


# In[27]:


response=marketing_dataset["Sales"]
predictors=marketing_dataset[["TV","Radio","Social Media", "Influencer_Macro", "Influencer_Mega", "Influencer_Micro",
                            "Influencer_Nano"]]


# In[28]:


import seaborn as sns
# Excluyo las dummy variables ya que son categoricas
correlation_matrix=marketing_dataset[["Sales", "TV", "Radio", "Social Media"]].corr()
correlation_matrix
sns.heatmap(correlation_matrix,vmin=0.0,vmax=1.0,annot=True) 


# In[29]:


predictors=marketing_dataset[["TV","Social Media", "Influencer_Macro", "Influencer_Mega", "Influencer_Micro",
                            "Influencer_Nano"]]


# In[30]:


from sklearn.model_selection import train_test_split
predictors_train, predictors_test, response_train, response_test = train_test_split(predictors, response, test_size=0.2, random_state=42)


# In[31]:


# En caso de haber multiple relacion lineal (>|0.8|) tendremos que excluir la variable ya que es un valor duplicado
# En este caso sacamos 'Radio'
correlation_matrix=marketing_dataset[["Sales", "TV", "Social Media"]].corr()
correlation_matrix
sns.heatmap(correlation_matrix,vmin=0.0,vmax=1.0,annot=True)


# In[32]:


# Evaluo mi modelo
import sklearn.linear_model as skl
linear_regression=skl.LinearRegression()
modelo = linear_regression.fit(predictors_train,response_train)


# In[33]:


print(linear_regression.coef_)
print(linear_regression.intercept_)


# In[34]:


entrada = [[68,2.056, 0, 0, 1, 0]]
modelo.predict(entrada)


# In[35]:


entrada = [[10,3.88, 1, 0, 0, 0]]
modelo.predict(entrada)


# In[42]:


#TV      Radio  Social Media Influencer       Sales
rating_TV=int(input("Ingrese rating de TV: "))
rating_social=float(input("Ingrese rating en redes sociales: "))
influencer=input("Ingrese el nombre del media influencer: ")


# In[37]:


entrada = [[rating_TV,rating_social, 0, 0, 0, 0]]

if influencer == "Macro":
    entrada[0][2] = 1
elif influencer == "Mega":
    entrada[0][3] = 1
elif influencer == "Micro":
    entrada[0][4] = 1
else:
    entrada[0][5] = 1
    
modelo.predict(entrada)


# In[38]:


r_squared=linear_regression.score(predictors,response)
r_squared


# In[39]:


# Residuals margen de error
response_predictions=linear_regression.predict(predictors)
residuals=response-response_predictions
print(residuals.mean())
residuals.std()


# In[40]:


import matplotlib.pyplot as plt
plt.hist(residuals,bins=100)
plt.show()


# In[41]:


from sklearn.metrics import mean_squared_error

y_pred=modelo.predict(predictors_test)
mse=mean_squared_error(response_test,y_pred)
print(mse)

