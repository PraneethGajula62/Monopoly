import Monopoly


class Player:
    def __init__(self, name = str, money = int, position = int, properties = list[Monopoly.TitleDeed], latest_roll = int):
        self.name = name 
        self.money = money
        self.position = position
        self.properties = properties
        self.latest_roll = latest_roll

    def __str__(self):
        return f"""Player: {self.name}"""
    
