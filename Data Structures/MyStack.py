# Use list to implement all Stakc's api.
class Stack:
    def __init__(self, size=1):
        self.stack = []
        self.size = size

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peak(self):
        return self.stack[-1]

    def pop(self):
        try:
            return self.stack.pop()
        except Exception as e:
            print(e)
            return False

    def push(self, item):
        try:
            self.stack.append(item)
            return True
        except Exception as e:
            print(e)
            return False
