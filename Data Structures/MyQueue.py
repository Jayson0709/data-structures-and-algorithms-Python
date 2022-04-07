# Simple implementation of a Queue's api using list
class Queue:
    def __init__(self, size=10):
        self.size = size
        self.queue = []

    def add(self, item):
        try:
            if len(self.queue) < self.size:
                self.queue.append(item)
                return True
            else:
                raise ValueError('Queue is full now.')
        except Exception as e:
            print(e)
            return False

    def element(self):
        return self.queue[-1]

    def peek(self):
        if self.queue is None:
            return None
        else:
            return self.queue[-1]

    def poll(self):
        if self.queue is None:
            return None
        else:
            return self.queue.pop()

    def remove(self):
        if self.queue is None:
            return None
        else:
            return self.queue.pop()
