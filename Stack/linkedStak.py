class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, dataOfNode):
        self.head = Node(dataOfNode, self.head)
        self.size +=1



    def pop(self):
        if self.head is None:
            return None
        popElement = self.head
        self.head = self.head.next
        self.size -= 1
        return popElement

    def peek(self):
        return self.head

    def len(self):
        return self.size

    def printMyStack(self):
        pass






myStack = LinkedStack()
myStack.push(41)
print(myStack.len())
myStack.push(51)
print(myStack.len())
myStack.pop()
print(myStack.len())
myStack.push(71)
myStack.push(51)
myStack.pop()
print(myStack.len())
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.len())
myStack.pop()
print(myStack.len())
print(myStack)
