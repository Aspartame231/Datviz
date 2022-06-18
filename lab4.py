import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
df=pd.read_csv('googleplaystore.csv')
d=df.head(200)
print(d)
sns.lineplot(x="Size",y="Rating",data=d,hue="Category",palette="hot", linestyle='dashdot', linewidth = 2, style="Category", marker='o',legend="brief")
plt.title("Variation of Rating of an App of various Categories with Size of an App") 
plt.xticks(rotation=90)
plt.show()