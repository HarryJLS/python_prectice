

def print_info(name, age=35):
    print(f'name: {name}')
    print(f'age: {age}')

print_info('顾安')
print_info('顾安', 18)

def test(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

def test1(a, b, *args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))



if __name__ == "__main__":
    print_info("test")
    test(11, 22, 33, 44, 55, 66, name='顾安', address='长沙')
    test1(11, 22, 33, 44, 55, 66)