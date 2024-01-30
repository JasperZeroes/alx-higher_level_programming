#Docstring documentation and Unit testing

#Unit testing
from math import pi

def area_of_circle(r):
    """ Computes the area of a circle of a given radius"""
    if type(r) not in [int, float]:
        raise TypeError("radius must be a non-negative real number")

    if not r >= 0:
        raise ValueError("radius cannot be a negative number")

    area = pi * (r ** 2)
    return area



#Docstring documentation
'''class Stack:
    """ Basic stack implementation.
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.pop()
    3
    >>> stack.peek()
    2
    >>> stack.is_empty()
    False
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

    def display_element_on_stack(self):
        i = 0
        if self.items != []:
            for elem in self.items:
                print(self.items[i], end='\t')
                i += 1
            print('\n')
        else:
           print("Stack is Empty.")

Note: For doctstring test, do not forget to add the line below;
        if __name__ == "__main__":
            import doctest
            doctest.testmod()
so as to enable you run it from the CLI using; 
        python3 filename.py
else use 
        python3 -v filemame.py directly from the CLI
        '''
