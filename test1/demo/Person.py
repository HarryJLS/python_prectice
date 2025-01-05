class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name[0]}')
        print(f'age: {self.age}')


if __name__ == "__main__":
    o = Person(["1", "2", "3"], 18)
    o.print_info()
