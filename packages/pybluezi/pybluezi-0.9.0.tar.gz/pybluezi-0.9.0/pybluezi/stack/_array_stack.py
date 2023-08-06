class _Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []
        self._name = self.__class__.__name__
    def __len__(self):
        return len(self._data)
    def _is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def pop(self):
        if self._is_empty():
            raise _Empty('Stack is empty!')
        return self._data.pop()
    def top(self):
        if self._is_empty():
            raise _Empty('Stack is empty!')
        return self._data[-1]
    def __str__(self):
        output = '['
        if self._is_empty():
            return output + ']'
        for i in range(len(self._data)):
            if i == len(self._data) - 1:
                output += str(self._data[i]) + ']'
            else:
                output += str(self._data[i]) + ', '
        return output
    def __repr__(self):
        output = self._name + '(['
        if self._is_empty():
            return output + '])'
        for i in range(len(self._data)):
            if i == len(self._data) - 1:
                output += str(self._data[i]) + '])'
            else:
                output += str(self._data[i]) + ', '
        return output
