# 实现hashtable,指定在key位置存入data
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # hold the key items
        self.data = [None] * self.size  # hold the data values

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:  # 如果slot内是empty，就存进去
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:  # slot内已有key
            if self.slots[hash_value] == key:  # 如果已有值等于key,更新data
                self.data[hash_value] = data  # replace
            else:  # 如果slot不等于key,找下一个为None的地方
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    print('while next_slot:', next_slot)
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                    print('slots None')
                else:
                    self.data[next_slot] = data
                    print('slots not None')

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        print('key:', key)
        print('data:', data)
        self.put(key, data)
