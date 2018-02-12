import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'Company': ['CompA','CompB','CompC','CompD','CompE'],
                    'Rating': [5.0,4.0,1.0,1.0,1.0]})
df = pd.concat([df, df, df, df, df])
print(df)
dummies = pd.get_dummies(df['Company'])
df = pd.concat([df[['Rating']], dummies], axis=1)
df = df.corr()
print(df)