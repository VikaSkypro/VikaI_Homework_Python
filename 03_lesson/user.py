class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        print("Имя: ", self.first_name)

    def printLname(self):
        print("Фамилия: ", self.last_name)

    def printFnameLname(self):
        print("Меня зовут", self.first_name, self.last_name)
