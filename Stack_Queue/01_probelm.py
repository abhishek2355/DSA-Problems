# Problem statement: Implement a stack using an array.

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.top += 1
        self.stack.append(data)

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.stack.pop(self.top+1)
    
    def Top(self):
        if self.top >= 0:
            return self.stack[self.top]
        

    def size(self):
        return self.top + 1
    


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top of stack is before deleting any element", s.Top())
print("Size of stack before deleting any element", s.size())
print("The element deleted is", s.pop())
print("Size of stack after deleting an element", s.size())
print("Top of stack after deleting an element", s.Top())
