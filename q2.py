size=int(input("Enter the size of the sequence"))
numbers=[]

for i in range (size):
    temp=int(input("Enter number"))
    if(temp%2==1):
        numbers.append(temp)

for i in range (len(numbers)):
    for j in range (i+1,len(numbers)):
        print(numbers[i],",",numbers[j])
