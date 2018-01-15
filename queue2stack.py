#how to create a queue using two stacks

class Queue2stack(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()
                        
