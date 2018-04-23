import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
col1=[]
col2=[]
for i in range(0,36):
    if i not in [28]:
        col1.append(c12.values[i][0])
        col2.append(c13.values[i][13]-c12.values[i][13])
val=pd.DataFrame(col2,index=col1,columns=['Difference'])
val.plot(kind='bar')
plt.xlabel('States/UT')
plt.ylabel('Change in crime rate')
plt.title('Difference of crime rate from 2012 t0 2013')
plt.show()
