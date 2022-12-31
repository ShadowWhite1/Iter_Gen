import types


def flat_generator(list_of_lists):
    x = -1
    while x < len(list_of_lists) - 1:
        x += 1
        y = -1
        while y < len(list_of_lists[x]) - 1:
            y += 1   
            yield list_of_lists[x][y]



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    # list_of_lists_1 = [
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ]
    # for i in flat_generator(list_of_lists_1):
    #     print(i)