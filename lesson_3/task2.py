class Stack:

    def __init__(self):
        self.myStack = []

    def push(self, new_item):
        self.myStack.append(new_item)
        print(self.myStack)

    def delete(self):
        self.myStack.pop()
        print(self.myStack)