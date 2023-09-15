import Monopoly


class Railroad(Monopoly.Property):
    def __init__(self, railroads_owned = int, mortgage = bool, mortgage_value = int):
        self.railroads_owned = railroads_owned
        current_railroads_owned = railroads_owned
        self.mortgage = mortgage
        self.mortgage_value = mortgage_value
#       old_rent = self.rent
#       list_of_railroads_owned = list[Railroad]
        list_of_rent_changes = ["List", "of", "Railroad", "Rents"]


    def __str__(self):
        print(f"""Railroad: {self.name}
                    Number owned: {self.railraods_owned}
                    Rent: {self.rent}""")

    def update_rent(self):
        counter = 0
        for i in Monopoly.AllProperties:
            if Monopoly.AllProperties[i].Railroads.owner != " ":
                counter += 1
        self.rent *= self.list_of_rent_changes[counter]
        