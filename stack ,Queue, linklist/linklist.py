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


s1 = LinkedList()
s1.append('A')
s1.append('B')
s1.append('C')
s1.append('D')
s1.append('E')
s1.append('F')
s1.insertAfter('X', 'C')
s1.insertAfter('Y', 'X')
s1.insertAfter('Z', 'Y')
print(s1)
