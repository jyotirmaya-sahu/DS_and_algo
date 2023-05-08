# Implementing stack using linked list

class Node:
    def __init__(self, val):
        self. value = val
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top is None:
            return None
        else:
            top = self.top
            self.top = top.next
            return top.value
    
    def peek(self):
        return self.top.value
    
    def display(self):
        currNode = self.top
        while (currNode is not None):
            print(currNode.value)
            currNode = currNode.next


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(7)
stack.push(18)
print(stack.peek())
stack.pop()
stack.pop()
print(stack.peek())
stack.display()