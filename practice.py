import pandas as pd
import numpy as np
df=pd.read_csv('athlete_events.csv')
indm=df.loc[df['Team']=='India']

m=indm['ID'][indm['Sex']=='M'].count()
f=indm['ID'][indm['Sex']=='F'].count()
print(m)
print(f)