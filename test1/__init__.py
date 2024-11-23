print("test")
# import precticeDemo.demo1
from precticeDemo import demo1

def test():
    a = 1
    print(a > 2)

if __name__ == "__main__":
    print("test1")
    test()
    demo1.print_test(1, 2)
    fruits = ["apple", "banana", "cherry"]
    for ff in fruits:
        print(ff)
    i = 0
    # while i < 10:
    #     print(i)
    #     i += 1
    for i in range(5):
        print(i)
