import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        sum = first + second
        print(f"You rolled a {first} and a {second}! You may move {sum} spaces!")
        return


dice = Dice()
dice.roll()