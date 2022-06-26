class ArrayStack:

    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        self.array.pop()

    def peek(self):
        return  self.array[len(self.array) - 1]

    def len(self):
        return len(self.array)

    def print(self):
        print(self.array)

    pass


myStack = ArrayStack()
myStack.push(45)
myStack.push(4)
myStack.pop()
myStack.print()
myStack.push(5)
myStack.push(54)
myStack.push(8)
myStack.pop()
myStack.print()
myStack.push(94)
myStack.push(42)
myStack.print()
myStack.pop()
myStack.print()
print(myStack.peek())


