from vpython import *
class Stack:
   def __init__(self):
    self.size=input("Enter size of the stack")
    self.stack={}
    self.pos=0
    self.bx=[]
    self.txt=[]
    self.y=-9
   def push(self,a):
     if(self.pos==self.size):
         text(text=str("The stack is full"), pos=vector(10,2,2), depth=0, color=color.green)
         #print("The stack is full")
     else:
         self.stack[self.pos]=a
         self.pos=self.pos+1
         self.y=self.y+3
         bx[self.pos]=box(pos=vec(0,self.y,0),size=vec(6,2,0), color=color.cyan)
         txt[self.pos]=text(text=str(a), pos=vector(0,y,0), depth=0, color=color.green)
         #print("Value entered")
   def pop(self):
       if(self.pos==0):
           text(text=str("No elements found"), pos=vector(10,2,2), depth=0, color=color.green)
       else:
           box(pos=vec(0,y,0),size=vec(6,2,0), color=color.black)
           text(text=str(self.stack[self.pos-1]), pos=vector(0,y,0), depth=0, color=color.black)
           self.y=self.y-3
           #a=self.stack[self.pos-1]
           del self.stack[self.pos-1]
           self.pos-=1
           #print("Popped:"+a)
   def Size(self):
       text(text=str(self.pos), pos=vector(10,2,2), depth=0, color=color.green)
   def clearstack(self):
       self.stack.clear()
       self.bx.clear()
       self.txt.clear()
       self.pos=0
       text(text=str("Stack Cleared"), pos=vector(10,2,2), depth=0, color=color.green)

mystack= Stack()
mystack.push('Cobra')
mystack.push('Anaconda')
mystack.Size()
mystack.pop()
mystack.clearstack()
mystack.pop()
