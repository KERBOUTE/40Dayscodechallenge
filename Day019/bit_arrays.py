class bitArray:

    def __init__(self, n):

        # divide by 32 because 1 index (1 bucket) will store upto 32 bits => info for 32 num
        self.arr = [0] * ((n >> 5) + 1)

    def get(self, pos):

        self.index = pos >> 5 # index of array (bucket of array) will be pos / 32
        self.bitpos = pos & 0x1F # actual bit pos in the selected bucket (index) , i % 32 = i & 0x1F

        flag = 1   # flag = 0000.....00001
        flag = flag << self.bitpos  # flag = 0000...010...000

        return self.arr[self.index] & flag  != 0 # this will return 1 or 0 depending on set or not

    def set(self, pos):

        self.index = pos >> 5 # index of array (bucket of array) will be pos / 32
        self.bitpos = pos & 0x1F # actual bit pos in the selected bucket (index), i % 32 = i & 0x1F

        flag = 1
        flag = flag << self.bitpos

        self.arr[self.index] |= flag   # Oring with mask will set at the given pos

    def pretty_print(self):
        print(self.arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    ba = bitArray(5)
    for i in range(len(arr)):
        ba.set(i)
    print(ba.get(10))
    ba.pretty_print()
