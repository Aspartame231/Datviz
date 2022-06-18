import pandas as pd 
import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 
data=pd.read_csv("googleplaystore.csv") 
print(data.columns) 
x=np.array(list(data['Category'].head(20))) 
y=np.array(list(data['Installs'].head(20))) 
z=np.array(list(data['App'].head(20))) 
data = {'Category': x,'Installs': y,'App': z} 
df = pd.DataFrame(data) 
print(df.columns) 
g=nx.from_pandas_edgelist(df,source='Category',target='App',edge_attr='Installs') 
plt.figure(1) 
nx.draw(g) 
plt.figure(2) 
nx.draw_networkx(g) 
plt.figure(3) 
nx.draw_circular(g) 
plt.figure(4) 
nx.draw_spring(g) 
plt.show() 
pos = nx.spring_layout(g) 
nodes = nx.draw_networkx_nodes(g, pos) 
nodes.set_edgecolor('yellow') 
nx.draw(g, node_color='b', width=3, with_labels=True) 
plt.show()