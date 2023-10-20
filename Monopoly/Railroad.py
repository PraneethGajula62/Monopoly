import Player
import PlayerAndProperty
import Master_List.AllRailroads as AllRailroads


class Railroad(PlayerAndProperty):
    def __init__(self, railroads_owned = int, mortgage = bool, mortgage_value = int):
        self.railroads_owned = railroads_owned
        current_railroads_owned = railroads_owned
        self.mortgage = mortgage
        self.mortgage_value = mortgage_value
#       old_rent = self.rent
#       list_of_railroads_owned = list[Railroad]
        list_of_rent_changes = ["These", "Are", "All", "Numbers"]

        same_color_deeds = []
        for i in AllRailroads.all_railroads:
            if i.color == self.color:
                same_color_deeds.append(i)
        self.same_color_deeds = same_color_deeds


    def __str__(self):
        print(f"""Railroad: {self.name}
                    Number owned: {self.railraods_owned}
                    Rent: {self.rent}""")

    def update_rent(self):
        counter = 0
        for i in AllRailroads.all_railroads:
            if AllRailroads.all_railroads[i].Railroads.owner != " ":
                counter += 1
        self.rent *= self.list_of_rent_changes[counter]

    def pay_up(self, payer = Player.Player, receiver = Player.Player):
        return None