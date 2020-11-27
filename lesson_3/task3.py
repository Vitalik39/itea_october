class Queue:

    def __init__(self):
        self.myQueue = []

    def push(self, new_item):
        self.myQueue.append(new_item)
        print(self.myQueue)

    def delete(self):
        self.myQueue.pop(0)
        print(self.myQueue)