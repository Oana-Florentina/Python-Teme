# Write a Python class that simulates a Queue.
# The class should implement methods like push, pop, peek
# (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())  # Removes and returns 1 (first element added)
print(queue.peek())  # Returns 2 (next element to be removed)
print(queue.pop())  # Removes and returns 2
print(queue.pop())  # Removes and returns 3
print(queue.pop())  # Returns None (queue is empty)
