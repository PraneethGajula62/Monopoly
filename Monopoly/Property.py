import Monopoly


class Property:
    def __init__(self, name = str, rent = int, mortgage = bool, owner = Monopoly.Player, position = int,):
        self.name = name
        self.rent = rent
        self.mortgage = mortgage
        self.owner = owner
        self.position = position


    def mortgage_square(self, player = Monopoly.Player):
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