class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age


    def print_info(self):
        print(f'name: {self.name[0]}')
        print(f'age: {self.__age}')


if __name__ == "__main__":

    o = Person(["1", "2", "3"], 18)
    o.set_age(89)
    o.print_info()