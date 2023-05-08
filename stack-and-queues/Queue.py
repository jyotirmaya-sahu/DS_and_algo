
class Node:
    def __init__(self, val):
        self. value = val
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None and self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    

    def dequeue(self):
        if (self.front is None):
            return None
        else:
            front = self.front
            if (self.front.next is None):
                self.rear = None
            self.front = self.front.next
            return front.value
    

que = Queue()
que.enqueue(2)
que.enqueue(3)
que.enqueue(5)
que.enqueue(8)
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
que.enqueue(8)
que.enqueue(5)
print(que.dequeue())
