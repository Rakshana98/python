import pandas as pd
import numpy as np

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
c12.sort_values(by="Total",ascending=False).head()
col1=[]
col2=[]
for i in range(0,36):
    col1.append(c12.values[i][0])
    col2.append(c13.values[i][13]-c12.values[i][13])
df=pd.DataFrame(col2,index=col1,columns=['Difference'])
df.sort_values(by='Difference',ascending=False).head()
df.sort_values(by='Difference').head()
