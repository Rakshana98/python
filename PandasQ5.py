import pandas as pd
import numpy as np

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
col1=[]
row1=[]
for i in range(0,36):
    col1.append(c12.values[i][0])
for i in range(0,10):
    row1.append(itact.values[i][1])
df=pd.DataFrame(np.nan,index=col1,columns=row1)
for i in range(0,10):
    val=[]
    for j in range(0,36):
        df.values[j][i]=c12.values[j][i+1]
df.to_csv('F:\VI SEM\total.csv', index=True)
