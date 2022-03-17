class Array(object):
    
    def __init__(self, size=64, init=None):
        self._size = size
        self._items = [init] * self._size
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return self._size
    
    def clear(self):
        for i in range(len(self._size)):
            self._items[i] = None

    def __iter__(self):
        for item in self._items:
            yield item    


class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    # Never being used
    UNUSED = None
    # Used previously, but deleted now.
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init = HashTable.UNUSED)
        self.length = 0
    
    def __len__(self):
        return self.length
    
    