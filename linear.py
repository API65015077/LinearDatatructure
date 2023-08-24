# Stack
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def __str__(self):
        s = "Stack of " + str(len(self.items)) + " items: "
        for i in self.items:
            s += str(i) + " "
        return s

# Linklist
class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def __str__(self):
        s = ""
        t = self.head
        while t != None:
            s += str(t.data) + " "
            t = t.next
        return s
    
    def insertAfter(self, data, after):
        data = Node(data)
        head = self.head
        # return head.data
        while head.data != after:
            head = head.next
        data.next = head.next
        head.next = data

# Queue
class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)



s1 = Stack([])
for i in range(6):
    s1.push(chr(ord('A') + i))
print("Stack =",s1.items)

for i in range(len(s1.items)+1):
    # print("--------------------")
    print("The Top of stack is",s1.peek())
    s1.pop()

print("s1 emty is",s1.isEmpty())

print("-------------------------------------------------")

s2 = Queue()
for i in range(6):
    s2.enqueue(chr(65+i))
print("This Queue have",s2.items)

for i in range(len(s2.items)):
    print("First Queue is",s2.dequeue())
print("This Queue have",s2.items)

print("-------------------------------------------------")

s3 = LinkedList()

for i in range(6):
    s3.append(chr(ord('A') + i))
print("Linklist =",s3)

s3.insertAfter('X', 'C')
s3.insertAfter('Y', 'X')
s3.insertAfter('Z', 'Y')
print("Linklist =",s3)

print("-------------------------------------------------")