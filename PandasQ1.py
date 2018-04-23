import pandas as pd

c12=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2012.csv')
c13=pd.read_csv('F:\VI SEM\Cyber+Crime_India_+2013.csv')
itact=pd.read_csv('F:\VI SEM\IT_Act.csv')
maxval=0
maxi=2
for i in range(1,13):
    val=0
    for j in range(1,38):
        val+=c12.values[j][i]
    if (maxval<val):
        maxval=val
        maxi=i
max12=c12.columns[maxi]
print("The category of crime often commited in 2012 is ",max12)
for j in range(0,10):
    if (c12.columns[maxi]==itact.values[j][0]):
        print ("It comes under ",itact.values[j][1]," of IT Act")
maxval=0
maxi=2
for i in range(1,13):
    val=0
    for j in range(1,38):
        val+=c13.values[j][i]
    if (maxval<val):
        maxval=val
        maxi=i
max13=c13.columns[maxi]
if (max12==max13):
    print("The crime occuring often in 2013 is the same")
else:
    print ("The crime occuring often in 2013 is not same, the one that is often in 2013 is ",max13)
