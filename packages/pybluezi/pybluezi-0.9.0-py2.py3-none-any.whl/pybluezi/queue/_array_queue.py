class _Empty(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 20
    def __init__(self):
        self._size = 0
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._name = self.__class__.__name__
    def __len__(self):
        return self._size
    def enqueue(self, e):
        if self._size == ArrayQueue.DEFAULT_CAPACITY:
            self._resize(2 * ArrayQueue.DEFAULT_CAPACITY)
        avail = (self._size + self._front) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def dequeue(self):
        if self._size == 0:
            raise _Empty('Queue is empty!')
        if 0 < self._size < (ArrayQueue.DEFAULT_CAPACITY // 4):
            self._resize(ArrayQueue.DEFAULT_CAPACITY // 2)
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value
    def front(self):
        if self._size == 0:
            raise _Empty('Queue is empty!')
        return self._data[self._front]
    def _is_empty(self):
        return self._size == 0
    def _resize(self, c):
        new_data = [None] * c
        w = self._front
        for i in range(self._size):
            new_data[i] = self._data[w]
            w = (w + 1) % len(self._data)
        self._data = new_data
        self._front = 0
        ArrayQueue.DEFAULT_CAPACITY = c
    def __str__(self):
        output = '['
        if self._size == 0:
            return output + '])'
        for i in range(self._size):
            index = (self._front + i) % len(self._data)
            if i == self._size - 1:
                output += str(self._data[index]) + ']'
            else:
                output += str(self._data[index]) + ', '
        return output
    def __repr__(self):
        output = self._name + '(['
        if self._size == 0:
            return output + '])'
        for i in range(self._size):
            index = (self._front + i) % len(self._data)
            if i == self._size - 1:
                output += str(self._data[index]) + '])'
            else:
                output += str(self._data[index]) + ', '
        return output
