import numpy as np
import pandas as pd
from scipy import stats 

#this will find the correlation between numerical and categorical information

#our data
infoList = [
('letters',['a','a', 'b', 'b','c','c']),
('numbers', [13, 51, 640, 600, 80, 90])
]
#showing another way to create a DataFrame:
df = pd.DataFrame.from_items(infoList)

#print out information about the DataFrame
print("DataFrame information:")
df.info()

#print out the contents 
print("DataFrame contents:")
print(df)

#From the documentation: get_dummies: Convert categorical variable into dummy/indicator variables
df_dummies = pd.get_dummies(df['letters'])

#look at it:
print("DataFrame dummies contents:")
print(df_dummies)

#add the dummies to the original DataFrame:
df_new = pd.concat([df, df_dummies], axis=1)

#look at it:
print("new DataFrame contents:")
print(df_new)

#delete 'letters' so that we actually get a correlation matrix:
df_new = df_new.drop(['letters'],axis=1)
#or:
#del df_new['letters']

#look at it:
print("new DataFrame contents:")
print(df_new)

#print out the correlation matrix:
print(df_new.corr())