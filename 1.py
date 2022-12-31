class FlatIterator:
    def __init__(self, list_of_list):
        self.start = 0
        self.end = len(list_of_list)
        self.list = list_of_list
    def __iter__(self):
        self.x = 0
        self.y = self.start - 1
        return self
    def __next__(self):
        self.y += 1
        if self.y <= len(self.list[self.x]) - 1:
            return self.list[self.x][self.y]
        else:
            self.x += 1
            self.y = 0
            if self.x == self.end:
                raise StopIteration
            else:
                return self.list[self.x][self.y]

                


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item 

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    # list_of_lists_1 = [
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]
    # for i in FlatIterator(list_of_lists_1):
    #     print(i)