# Write a Python class that simulates a Stack.
# The class should implement methods like push, pop, peek
# (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Removes and returns 3
print(stack.peek())  # Returns 2 (top element)
print(stack.pop())  # Removes and returns 2
print(stack.pop())  # Removes and returns 1
print(stack.pop())  # Returns None (stack is empty)
