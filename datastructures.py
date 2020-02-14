class Stack:                       # implementation of stack
    def __init__(self):
         self.items = []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
         return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s=Stack()
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


class Queue:                             # implementation of Queue
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.dequeue()
q.dequeue()
print(q.size())


class Deque:                     # implementing Deque
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d=Deque()
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())