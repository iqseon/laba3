class mystring(str):
    def append(self, character):
        self += character

    def pop(self):
        if len(self) == 0:
            raise IndexError("pop from empty string")
        else:
            last_char = self[-1]
            self = self[:-1]
            return last_char
