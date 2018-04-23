from vpython import *
cord=[]
class Tree:
    val = None
    left = None
    right = None

    def __init__(self, val,coor=None):
        self.val = val
        if coor == None:
            self.x=0
            self.y=15
            self.z=0
            self.node=sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.red)
            text(text=str(val), pos=vector(self.x,self.y + 1, 0), depth=0, color=color.blue)
            cord.append(self)
        else:
            self.x, self.y, self.z = coor
            self.node = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.red)
            text(text=str(val), pos=vector(self.x,self.y + 1, 0), depth=0, color=color.blue)
            cord.append(self)
    # def check(self,val):
    #     if self.val==val:
    #         s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
    #         time.sleep(0.4)
    #         s1.visible = False
    #     elif val>self.val:
    #         s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
    #         time.sleep(0.4)
    #         s1.visible = False
    #         self.right.check(self.va)
    #

    def find(self, data, parent=None):
        if data < self.val:
            if self.left is None:
                return None, None
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.2)
            s1.visible = False
            return self.left.find(data, self)
        elif data > self.val:
            if self.right is None:
                return None, None
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.2)
            s1.visible = False
            return self.right.find(data, self)
        else:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.green)
            time.sleep(2)
            s1.visible = False
            return self, parent

    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is not None:
                    self.left.insert(val)
                else:
                    x = self.x - 10
                    y = self.y - 5
                    for cr in cord:
                        if cr.x==x and cr.y==y:
                            y=y-4
                    self.left = Tree(val,coor=(x,y, 0))
                    text(text=str(val), pos=vector(x,y + 1, 0), depth=0, color=color.yellow)
                    curve(pos=[(self.x, self.y, self.z), (x, y, 0)], radius=0.1)

            elif val > self.val:
                if self.right is not None:
                    self.right.insert(val)
                else:
                    x = self.x + 10
                    y = self.y - 5
                    for cr in cord:
                        if cr.x==x and cr.y==y:
                            y=y-4
                    self.right = Tree(val,coor=(x,y,0))
                    text(text=str(val), pos=vector(x,y + 1, 0), depth=0, color=color.yellow)
                    curve(pos=[(self.x, self.y, self.z), (x, y, 0)], radius=0.1)
            else:
                return
        else:
            self.val = val
            print("new node added")
    def inorder(self):
        if self.left:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.left.inorder()
        print (self.val, end=' ')
        s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.green)
        time.sleep(0.4)
        if self.right:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.right.inorder()
    def res(self):
        if self.val:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.red)
        if self.left:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.red)
            self.left.res()
        if self.right:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.red)
            self.right.res()
    def printPreorder(self):


        if self.val:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            print(self.val,end=' ')
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.green)
            time.sleep(0.4)
        if self.left:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.left.printPreorder()
        if self.right:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.right.printPreorder()

    def postorder(self):

        if self.val:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
        if self.left:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.left.postorder()
        if self.right:
            s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.blue)
            time.sleep(0.4)
            s1.visible = False
            self.right.postorder()
        print(self.val,end=' ')
        s1 = sphere(pos=vector(self.x, self.y, self.z), radius=1, color=color.green)
        time.sleep(0.4)


    def showTree(self):
        if self.left is not None:
            self.left.showTree()
        print(self.val, end = ' ')
        if self.right is not None:
            self.right.showTree()
