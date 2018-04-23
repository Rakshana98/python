import pandas as pd
import numpy as np

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
cols=[]
rows=[]
for i in range(1,14):
    cols.append(c12.columns[i])
for i in range(0,38):
    rows.append(c12.values[i][0])
df=pd.DataFrame(np.nan,index=rows,columns=cols)
for i in range(0,13):
    val=[]
    for j in range(0,38):
        df.values[j][i]=(c12.values[j][i+1]+c13.values[j][i+1])
df.to_csv('F:\VI SEM\consolidated.csv', index=True)
