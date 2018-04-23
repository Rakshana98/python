x=int(input("Enter x"))
f = open("sample.txt","r")
lines = f.readlines()
thisline=[]
for i in lines:
    thisline = i.split(" ")
for i in range(len(thisline)):
    temp=thisline[i]
    if len(temp)>x:
        print(temp)
