class _Empty(Exception):
    pass

class ArrayDeque:
    DEFAULT_CAPACITY = 20
    def __init__(self):
        self._length = 0
        self._front = 0
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._name = self.__class__.__name__
    def __len__(self):
        return self._length
    def add_last(self, e):
        if self._length < (len(self._data) // 4):
            self._resise(ArrayDeque.DEFAULT_CAPACITY // 2)
        if self._length == ArrayDeque.DEFAULT_CAPACITY:
            self._resise(2 * ArrayDeque.DEFAULT_CAPACITY)
        avail = (self._front + self._length) % len(self._data)
        self._data[avail] = e
        self._length += 1
    def add_first(self, e):
        if self._length < (len(self._data) // 4):
            self._resise(ArrayDeque.DEFAULT_CAPACITY // 2)
        if self._length == ArrayDeque.DEFAULT_CAPACITY:
            self._resise(2 * ArrayDeque.DEFAULT_CAPACITY)
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._length += 1
    def delete_last(self):
        if self._length == 0:
            raise _Empty('deque is empty!')
        back = (self._front + self._length - 1) % len(self._data)
        value = self._data[back]
        self._data[back] = None
        self._length -= 1
        return value
    def delete_first(self):
        if self._length == 0:
            raise _Empty('deque is empty!')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._length -= 1
        return value
    def _resise(self, c):
        new_data = [None] * c
        walk = self._front
        for i in range(self._length):
            new_data[i] = self._data[walk]
            walk = (walk + 1) % len(self._data)
        self._data = new_data
        ArrayDeque.DEFAULT_CAPACITY = c
        self._front = 0
    def __str__(self):
        output = '['
        if self._length == 0:
            return output + ']'
        for i in range(self._length):
            index = (self._front + i) % len(self._data)
            if i == self._length - 1:
                output += str(self._data[index]) + ']'
            else:
                output += str(self._data[index]) + ', '
        return output
    def __repr__(self):
        output = self._name + '(['
        if self._length == 0:
            return output + '])'
        for i in range(self._length):
            index = (self._front + i) % len(self._data)
            if i == self._length - 1:
                output += str(self._data[index]) + '])'
            else:
                output += str(self._data[index]) + ', '
        return output
