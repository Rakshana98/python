import pandas as pd

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
minval=9999
mini=2
for i in range(1,38):
    if (c13.values[i][13]==0):
        continue
    else:
        if (c13.values[i][13]<minval):
            minval=c13.values[i][13]
            mini=i
min13=c13.values[mini][0]
print (min13)
