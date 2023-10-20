import PlayerAndProperty
import Player
import Master_List.AllUtilities as AllUtilities

class Utility(PlayerAndProperty):
    def __init__(self, mortgage = bool, mortgage_value = int, other_owned = bool):
            multiplier = self.rent
            self.mortgage = mortgage
            self.mortgage_value = mortgage_value
            self.other_owned = other_owned = True


    def __str__(self):
          print(f"""Utility: {self.name}
                    Number owned: {int(self.other_owned)}
                    Multiplier: {self.multiplier}""")
          
    def update_multiplier(self):
           self.multipllier = 10
           # should happen when "Property" gets "bought", so function of "Property" should check if other "Utility" is bought upon buying or trading it and then call this function.
          
    def pay_up(self, payer = Player.Player, receiver = Player.Player):
           payer.money -= payer.latest_roll * self.multiplier
          