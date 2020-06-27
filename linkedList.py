class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def insertList(self, values):
        for value in values:
            self.insert(value)

    def delete(self, value):
        currentNode = self.head
        if currentNode.value == value:
            self.head = currentNode.nextNode
        else:
            while currentNode:
                nextNode = currentNode.nextNode
                if nextNode.value == value:
                    currentNode.nextNode = nextNode.nextNode
                    currentNode = None
                else:
                    currentNode = nextNode

    def __str__(self):
        printedList=''
        currentNode = self.head
        while currentNode is not None:
            printedList+=str(currentNode.value) + '->'
            currentNode = currentNode.nextNode
        printedList+='None'
        return printedList


linkedList = LinkedList()
linkedList.insertList([1, 2, 3, 4, 5, 6])
print(linkedList)
linkedList.delete(5)
linkedList.delete(6)
linkedList.delete(1)
print(linkedList)
