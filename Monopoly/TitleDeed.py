from Python Practice import Monopoly


class TitleDeed(Monopoly.Property):
    def __init__(self, color = str, monopoly = bool, houses = int, hotel = bool, mortgage = int, house_cost = int, hotel_cost = int, mortgage_value = int, all_deeds = Monopoly.AllDeeds):
        self.color = color
        self.monopoly = monopoly
        self.houses = houses
        self.hotel = hotel
        self.mortgage = mortgage
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost
        self.mortgage_value = mortgage_value
        same_color_deeds = []
        for i in all_deeds:
            if i.color == self.color:
                same_color_deeds.append(i)
        self.same_color_deeds = same_color_deeds

    def __str__(self):
        return f"""Title Deed: {self.name}
                    Color: {self.color}
                    Rent: {self.rent}"""
    
    def buy_house(self):
        if (self.same_color_deeds[0].houses == self.houses and self.same_color_deeds[1].houses == self.houses) or self.monopoly:
            self.owner.money -= self.house_cost
            self.houses += 1
            return
        
    def sell_house(self):
        if (self.same_color_deeds[0].houses == self.houses and self.same_color_deeds[1].houses == self.houses) or self.monopoly:
            self.owner.money += 0.5 * self.house_cost
            self.houses -= 1
            return
        
    def buy_hotel(self):
        if self.houses == 4 and (self.same_color_deeds[0].houses == self.houses and self.same_color_deeds[1].houses == self.houses):
            self.owner.money -= self.hotel_cost
            self.hotel += 1
            return
        
    def sell_hotel(self):
        if self.houses == 4 and (self.same_color_deeds[0].houses == self.houses and self.same_color_deeds[1].houses == self.houses):
            self.owner.money += 0.5 * self.hotel_cost
            self.hotel -= 1
            return
    
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

    def unmortgage_square(self, player = Monopoly.Player):
        if not self.mortgage:
            print("This property is not mortgaged!")
            return
        else:
            player.money -= (self.mortgage_value * 1.1)
            self.morgage = False
            return