import matplotlib.pyplot as plt 
import matplotlib.colors as clr 
import pandas as pd 
import numpy as np 
data = pd.read_csv('googleplaystore.csv') 
x = np.array(list(data['App'].head(50))) 
y = np.array(list(data['Installs'].head(50))) 
figure, (axes2) = plt.subplots(ncols=1) 
axes2.set_title("Number of Installs of an App") 
plt.plot(x, y, color='mediumturquoise', marker='d') 
plt.xlabel('App') 
plt.xticks(rotation=90)
plt.ylabel('Number of Installs') 
plt.legend(loc=0) 
plt.grid(True) 
plt.show() 