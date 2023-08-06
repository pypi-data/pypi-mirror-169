import ctypes

class DynamicArray:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._data = self._make_array(self._capacity)
        self._name = self.__class__.__name__
    def __len__(self):
        return self._length
    def __getitem__(self, k):
        if k < 0:
            k += self._length
            k = k % self._length
        if not 0 <= k <= self._length - 1:
            raise IndexError('Index out of range!')
        return self._data[k]
    def __setitem__(self, k, value):
        if k < 0:
            k += self._length
            k = k % self._length
        if not 0 <= k < self._length:
            raise IndexError('Index out of range!')
        self._data[k] = value
    def append(self, e):
        if 0 < self._length < (self._capacity // 4):
            self._resize(self._capacity // 2)
        if self._length == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._length] = e
        self._length += 1
    def extend(self, k):
        for e in k:
            self.append(e)
    def index(self, k):
        for i in range(self._length):
            if k == self._data[i]:
                return i
        return None
    def insert(self, k, e):
        if 0 < self._length < (self._capacity // 4):
            self._resize(self._capacity // 2)
        if self._length == self._capacity:
            self._resize(self._capacity * 2)
        if (not(0 <= k < self._length)) and k != 0:
            raise IndexError('Index out of range!')
        for i in range(self._length, k, -1):
            self._data[i] = self._data[i - 1]
        self._data[k] = e
        self._length += 1
    def remove(self, k):
        for i in range(self._length):
            if self._data[i] == k:
                for i in range(k, self._length - 1):
                    self._data[i] = self._data[i + 1]
                self._data[self._length - 1] = None
                self._length -= 1
                return
        raise ValueError('k not in list')
    def pop(self, k=None):
        if k is None:
            k = self._length - 1
        if not 0 <= k < self._length:
            raise IndexError('Index out of range!')
        value = self._data[k]
        self.remove(self._data[k])
        return value
    def _resize(self, c):
        new_array = self._make_array(c)
        for i in range(len(self)):
            new_array[i] = self[i]
        self._data = new_array
        self._capacity = c
    def _make_array(self, c):
        return (c * ctypes.py_object)()
    def __str__(self):
        output = '['
        if len(self) == 0:
            return output + ']'
        for i in range(len(self)):
            if i == (len(self) - 1):
                output += str(self[i]) + ']'
            else:
                output += str(self[i]) + ', '
        return output
    def __repr__(self):
        output = self._name + '(['
        if len(self) == 0:
            return output + '])'
        for i in range(len(self)):
            if i == (len(self) - 1):
                output += str(self[i]) + '])'
            else:
                output += str(self[i]) + ', '
        return output
