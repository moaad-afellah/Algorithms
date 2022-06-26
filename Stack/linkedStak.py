class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedStack:

    def __init__(self):
        self.head = []

    def push(self, dataOfNode):
        node = Node(dataOfNode, None)
        if len(self.listOfNode) > 1:
            node = Node(dataOfNode, node)
        self.listOfNode.append(node.data)
        return node


    def pop(self, head):
        current = head
        current = current.next
        self.listOfNode.remove(head.data)

    def peek(self):
        return self.listOfNode[len(self.listOfNode) - 1]

    def len(self):
        listOfNode = 0
        while listOfNode < len(list):
            listOfNode = listOfNode + 1
        print("Len of this list is: ", listOfNode)

    def print(self):
        print(self.listOfNode)



myStack = LinkedStack()
myStack.len()
head = myStack.push(41)
head = myStack.push(51)
head = myStack.push(71)
head = myStack.push(1)
head = myStack.push(1)
head = myStack.push(1)
head = myStack.push(1)
head = myStack.push(1)
head = myStack.push(1)

