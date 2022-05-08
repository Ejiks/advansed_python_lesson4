nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list_inv = [
    [['a', [10, [[[20]]]]], 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
class MyIterator:

    def __init__(self, nested_list):
        self.nested_list = self.field_lst(nested_list)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        try:
            self.cursor += 1
            return self.nested_list[self.cursor - 1]
        except:
            raise StopIteration

    def field_lst(self, nested_list: list):
        new_lst = []
        for item in nested_list:
            if type(item) == list:
                new_lst += self.field_lst(item)
            else:
                new_lst.append(item)
        return new_lst

def my_gen(nested_list):
    for item in nested_list:
        if isinstance(item, list):   
            for nested_item in my_gen(item):
                yield nested_item
        else:
            yield item

if __name__ == '__main__':
    my_nested_list = MyIterator(nested_list)
    for item in my_nested_list:
        print(item)

    print("="*50)

    my_nested_list = MyIterator(nested_list_inv)
    for item in my_nested_list:
        print(item)

    print("="*50)

    flat_list = [item for item in my_nested_list]
    print(flat_list)

    print("="*50)

    for item in my_gen(nested_list):
        print(item)

    print("="*50)

    for item in my_gen(nested_list_inv):
        print(item)

  