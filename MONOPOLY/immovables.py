from card import *


class immovables(card):
    def __init__(self, num, name, price, owner, house_amount, rent, coordinates, center):
        card.__init__(self, num, name, coordinates, center)
        self.price = price
        self.owner = owner
        self.house_amount = house_amount
        self.rent = rent

    def get_price(self):
        return self.price + self.house_amount * 500
