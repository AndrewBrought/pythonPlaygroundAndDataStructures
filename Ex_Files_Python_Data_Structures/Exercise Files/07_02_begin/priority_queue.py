"""
Python Data Structures - A Game-Based Approach
Priority Queue Data Structure Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        # We used self.elements instead of self.items because it's not just items - it's items
        # and their associated priority

        # This pushes an element onto our Priority Queue, and it's going to do so in such a way that
        # it preserves the required ordering of our priority queue so that we would always be able
        # to access the minimum value based on that priority that we've passed in
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        # This gives us human readable representation of what's going on inside our object
        return str(self.elements)


# Now we look at the methods in action

if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    # We're going to be putting 2 things on our priority queue: value and a priority associated
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)

    # import to note that the order we have the items arranged does not matter because they are
    # stored according to the item's priority
    # The only thing we can guarantee about this output is that the item with the highest priority
    # will be on the left-hand side...the rest we can't guarantee where they're going to be
    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())
    # We put the index (ln 27) after self.elements in the get method to make sure we only return
    # the element itself and not the index value as well


