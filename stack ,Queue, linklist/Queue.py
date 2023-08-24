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

s1 = Queue()

for i in range(6):
    s1.enqueue(chr(65+i))
print("This Queue have",s1.items)

for i in range(len(s1.items)):
    print("First Queue is",s1.dequeue())
print("This Queue have",s1.items)