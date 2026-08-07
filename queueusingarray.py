import numpy as np
class queue:
    def __init__(self,size):
        self.size=size
        self.queue=np.empty(size,dtype=int)
        queue.front=-1
        queue.rear=-1
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("Queue Overflow")
        else:
            if self.front==-1:
                self.front=0
            self.rear=self.rear+1
            self.queue[self.rear]=item
            print(item, " inserted!")
    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            print("Stack Underflow")
        else:
            item=self.queue[self.front]
            self.front=self.front+1
            print(item," removed!")
            if self.front>self.rear:
                self.front=-1
                self.rear=-1
    def peek(self):
        if self.front==-1:
            print("Queue is Empty!")
        else:
            print("Elements in Queue are: ", self.queue[self.front])
    def display(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
q=queue(4)
q.enqueue(24)
q.enqueue(12)
q.enqueue(200)
q.enqueue(3)
q.display()
q.dequeue()
q.dequeue()
q.enqueue(3)
q.peek()
q.display()
