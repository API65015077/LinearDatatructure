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
            return self.items.pop(-1)
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
    
s1 = Stack([])
print(s1.items)
for i in range(6):
    s1.push(chr(ord('A') + i))
print(s1.items)

# for i in range(len(s1.items)):
#     s1.pop()
#     print("--------------------")
#     print(s1.peek())
#     print("--------------------")

# print("s1 emty is",s1.isEmpty())
print(s1.pop())