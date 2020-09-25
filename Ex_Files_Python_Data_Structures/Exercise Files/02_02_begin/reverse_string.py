"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.

# The suggestion is to use a while loop
# The obvious logic would be to pop off the letters one at a time, given the string size and add them to a 'bucket' of
# some sort, in this case, looks like reversed_string

"""
Since I am new to the python syntax, Ill sudo code in Java. My solution would very roughly be something like:

int i = 0;
while(i < string.size()) {
    reversed_string += string.pop();
    i++
}
return reversed_string
"""


for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

"""
Here we added each character from our string to our stack first...I missed that, THEN we used the pop()
to add one character at a time 'backwards' to a new string.
One take away is that - in thinking about java and how it compares, there a lot of methods taken for granted 
that we are having to include and build in python...I am not sure if this is necessary or more of a bare-bones ground up 
approach, but it's very helpful to see it in this way.

Two different types of iteration are present: FOR and WHILE
General thinking is that when you care about the length or individual indices, you use a For loop, 
the conditional iteration is WHILE, when your program doesn't know how long/big the stack is, we use a more vague - 
while the stack is not empty 
"""

print(reversed_string)
