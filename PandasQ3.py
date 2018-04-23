import pandas as pd

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
tot12=c12.values[37][13]
tot13=c13.values[37][13]
if (tot12<tot13):
    print ("increasing")
elif (tot12>tot13):
    print ("decreasing")
else:
    print ("equal")
