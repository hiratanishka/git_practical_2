import numpy as np
class stack:
    def __init__(self,size):
        self.size=size
        self.stack=np.empty(size,dtype=int)
        self.top=-1
    def push(self,item):
        if self.top==self.size-1:
            print("Stack Overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=item
            print(item," inserted!")
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
        else:
            item=self.stack[self.top]
            self.top=self.top-1
            print(item," removed!")
    def peek(self):
        if self.top==-1:
            print("Stack is empty!")
        else:
            print("Top element in the stack is ", self.stack[self.top])
    def display(self):
        if self.top==-1:
            print("Stack is empty!")
        else:
            print("Elements in the stack are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
s=stack(4)
s.push(24)
s.push(12)
s.push(200)
s.push(3)
s.display()
s.pop()
s.pop()
s.push(3)
s.peek()
s.display()
