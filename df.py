import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,labels)
print (df)
###########################
df.replace({'yes':'true','no':'false'},inplace=True)
print(df)
#######################
a=np.array([0,0,0,0,0,0,0,0,0,0],float)
print(a)
a[6]=11
print(a)
##################################
a2=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],float)
print(a2)
for i in range(1,5):
    for j in range(1,5):
        a2[i,j]=0
print(a2)
##################################
t=np.arange(5)
s=[772.559998,776.429993,776.469971,776.859985,775.080017]
s=np.array(s)
plt.plot(t, s)
plt.xlabel('Date')
plt.ylabel('Close')
plt.title('Closing value of Alphabet Inc')
plt.grid(True)
plt.xticks(t,('03-10-16','04-10-16','05-10-16','06-10-16','07-10-16'))
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off')
plt.show()
################################
n=8
t1=[ 3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477]
t2=[ 11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847]
t3=[ 3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433]
t4=[ 4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]
t1=np.array(t1)
t2=np.array(t2)
t3=np.array(t3)
t4=np.array(t4)
ind = np.arange(n)    # the x locations for the groups
width = 0.35
p1 = plt.bar(ind, t1, width)
p2 = plt.bar(ind, t2, width,bottom=t1)
p3 = plt.bar(ind, t3, width,bottom=t1+t2)
p4 = plt.bar(ind, t4, width,bottom=t1+t2+t3)
plt.ylabel('Scores')
plt.title('Scores by group')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5','G6','G7','G8'))
plt.yticks(np.arange(0, 13, 1))
plt.legend((p1[0], p2[0],p3[0],p4[0]), ('t1', 't2','t3','t4'))
plt.show()
