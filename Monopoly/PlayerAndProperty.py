import Master_List.AllProperties as AllProperties


class Property:
    pass


class Player:
    def __init__(self, name = str, money = int, position = int, properties = list[Property], latest_roll = int):
        self.name = name 
        self.money = money
        self.position = position
        self.properties = properties
        self.latest_roll = latest_roll

    def __str__(self):
        return f"""Player: {self.name}"""


class Property:
    def __init__(self, name = str, rent = int, mortgage = bool, owner = Player, position = int, all_properties = AllProperties.all_properties):
        self.name = name
        self.rent = rent
        self.mortgage = mortgage
        self.owner = owner
        self.position = position
    


    def mortgage_square(self, player = Player()):
        if self.mortgage:
            print("Already mortgaged!")
            return
        else:
            if self.hotel or self.houses != 0:
                player.money += self.mortgage_value
                self.mortgage = True
                return
            else:
                print("Sell your hotels and houses first!")



