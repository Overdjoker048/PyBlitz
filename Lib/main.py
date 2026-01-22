from sys import stdout

def printf(output: str) -> None:
    stdout.write(output)

class array:
    __slots__ = ("__data", "__slots", "__size", "__mask", "__fmt")
    def __init__(self, slots: int, size: int, format=None):
        if size not in (1, 2, 4, 8):
            raise ValueError("size must be 1, 2, 4 or 8 bits")
        if slots <= 0:
            raise ValueError("slots must be positive")

        self.__slots = slots
        self.__size  = size
        self.__mask  = (1 << size) - 1
        self.__fmt   = format if format not in (None, int) else None
        self.__data  = bytearray((slots * size + 7) >> 3)

    def __len__(self) -> int:
        return self.__slots

    def __getitem__(self, i: int):
        if i < 0:
            i += self.__slots
        if not (0 <= i < self.__slots):
            raise IndexError

        bit = i * self.__size
        shift = 8 - self.__size - (bit & 7)

        val = (self.__data[bit >> 3] >> shift) & self.__mask
        return self.__fmt(val) if self.__fmt else val

    def __setitem__(self, i: int, value: int) -> None:
        if i < 0:
            i += self.__slots
        if not (0 <= i < self.__slots):
            raise IndexError

        if not isinstance(value, int):
            value = int(value, 0)

        if value & ~self.__mask:
            raise ValueError(f"value exceeds {self.__size} bits")
        
        bit = i * self.__size
        byte = bit >> 3
        shift = 8 - self.__size - (bit & 7)
        mask = self.__mask << shift
        self.__data[byte] = (self.__data[byte] & ~mask) | (value << shift)

    def __str__(self):
        return "|" + ", ".join(str(self[i]) for i in range(self.__slots)) + "|"
