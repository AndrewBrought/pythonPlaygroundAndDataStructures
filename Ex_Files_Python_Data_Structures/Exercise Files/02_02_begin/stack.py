"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/

NOTES:
we use pass while we have an empty class/function definition so that we don't get an error when we run the code
init is the object constructor - in this case we're creating an object called a stack.
This object is based on the template, which is the stack class - sounding sim. to java

self.items means the items property of the object we're creating...think public/private String hello; in java


"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items
        # both mean the same thing but the latter is more syntactically used

    def push(self, item):
        # this is a standard list method
        self.items.append(item)

    def pop(self):
        # this is a standard list method
        return self.items.pop()

    # basically we're taking a list and all of the associated methods and wrapping them in our own stack class (
    # abstraction) so that we can use the terms that we want and control how we interface with the list

    def peek(self):
        return self.items[-1]
        # in python and some other languages, we can access the end of a list by using negative indices
        # in java this is done: list.get(list.size() -1);
        # I am enjoying python's brevity of syntax

    def size(self):
        return len(self.items)

    def __str__(self):
        # this enables us to use the print statement to inspect our stack
        return str(self.items)


# this means, if we wanted to import this stack class into another file it could be a problem if we have code defined
# here, because it would also run in our imported file This states: if this is the main file that is being run,
# then execute code from line 55 onwards, if not just use the class and ignore the code below this is like public
# static void main in java - but with greater intuition
if __name__ == "__main__":
    # here we're instantiating a new stack s by calling the stack constructor Stack()
    s = Stack()
    print(s)
    # this gives us an empty list, which is what we were expecting, we haven't added anything to it
    print(s.is_empty())
    #     True
    s.push(3)
    print(s)
    s.push(5)
    s.push(7)
    print(s)

    print(s.pop())
    #     pop() does two things, removes an item from the list, and returns what that item is, in this case - 7
    print(s)

    print(s.peek())
    # this just reveals what is at the top of our list (what's last)

    print(s.size())
#     this reveals the count of indices in our list - there are 2 after we popped off 7

# useful tip: when finished with a section, reformat code to clean it up a bit
