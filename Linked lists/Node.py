import random


class Node:
    def __init__(self, data , next):
        self.data = data
        self.next = next


def createRandomListOfNode():

    node = Node(random.randint(-10, 10), None)
    for i in range(0, random.randint(0, 20)):
        node = Node(random.randint(-10, 10), node)
    return node


def createListOfNode():
    n4 = Node(random.randint(-10, 10), None)
    n3 = Node(random.randint(-10, 10), n4)
    n2 = Node(random.randint(-10, 10), n3)
    n1 = Node(random.randint(-10, 10), n2)
    return n1


def printlist(Head):
    listAsArray = []
    curent = Head
    while curent  != None:
        listAsArray.append(str(curent.data))
        curent = curent.next

    print (' --> '.join(listAsArray))
    return listAsArray


def searchForElement(head , element):
    curent = head
    while curent != None:
        if curent.data == element:
            return True
        curent = curent.next

    return False


def appendInHead(haed, newdata):
    return Node(newdata, haed)


def lenghtOfList(list):
    lenOFList = 0
    while lenOFList < len(list):
        lenOFList = lenOFList + 1
    print("Len of this list is: ", lenOFList)


def appendInTail(head, newdata):
    newNod = Node(newdata, None)
    curent = head
    while True:
        if curent.next == None:
            curent.next = newNod
            break
        curent = curent.next

def removeNode(head, data):
    if head is None:
        return None

    current = head
    if current.data == data:
        current = current.next
        return current

    flag = False
    while current is not None:
        if current.data == data:
            flag = True
            break
        previousNode = current
        current = current.next

    if flag:
       previousNode.next = current.next
    return head



head = createRandomListOfNode()
printlist(head)
print(searchForElement(head, 10))
head = appendInHead(head, 2)
listAsArray = printlist(head)
lenghtOfList(listAsArray)
appendInTail(head, 23)
printlist(head)
while True:
    number = int(input(":"))
    head = removeNode(head, number)
    printlist(head)

