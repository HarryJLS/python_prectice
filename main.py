# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import TestClassDemo

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    print('测试')# Press Ctrl+F8 to toggle the breakpoint.

class Test():
    def __print__(self, name):
        print('测试看看')
        print(name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    t = TestClassDemo.TestClass()
    t.print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
