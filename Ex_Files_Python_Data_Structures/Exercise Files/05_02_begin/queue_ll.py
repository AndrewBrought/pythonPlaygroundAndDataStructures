"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        # This is a constructor for a deque
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        # This is a method of the deque class, if this was a list we would do
        # pop([0]) - pop the item at the 0 index but popleft method is from the deque class, behaves
        # exactly the same way, just faster
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("D")
    q.enqueue("F")
    print(q)
    # The reason we can print the dequeue method without calling it first is because
    # it does two things, it removes an item from the queue and it returns it
    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)

    a = Queue()
    a.enqueue("Learning")
    a.enqueue("with")
    a.dequeue()
    a.enqueue("Linked")
    a.enqueue("In")
    a.dequeue()
    print(a)