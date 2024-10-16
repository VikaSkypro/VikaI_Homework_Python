class Address:

    def __init__(self, index, city, street, building, room):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.room = room

    def __str__(self):
        return (f"{self.index}, {self.city},"
                f" {self.street}, {self.building} - {self.room}")
