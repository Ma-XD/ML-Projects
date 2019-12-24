import random
import copy
import transformer
from picture import Picture

class player:
    def __init__(self, name, money, immov, position, is_bankrupt, mess_coor, field_obj, bank_obj):
        self.name = name
        self.money = money
        self.immov = immov
        self.position = position
        self.is_bankrupt = is_bankrupt
        self.mess_coor = mess_coor
        self.field_obj = field_obj
        self.bank_obj = bank_obj
        self.pics = [transformer.transform(Picture("Figures1.jpg"), 40, 20), transformer.transform(Picture("Figures2.jpg"), 40, 20)]

    def get_immovables_price(self):
        price = 0
        for imm in self.immov:
            price += imm.get_price()
        return price

    #def get_con(self):
    #    cube1 = random.randrange(1, 7)
    #    cube2 = random.randrange(1, 7)
    #    return [cube1, cube2]

    def sell_immov(self, diff):
        sum = 0
        while sum < diff and len(self.immov) > 0:
            imm = copy.deepcopy(self.immov.pop(0))
            sum += int(imm.price / 5)
            self.bank_obj.buy_immovable(imm.price, imm.num)
        return sum

    def pay(self, price):
        if self.money < price:
            self.money += self.sell_immov(price - self.money)
        if self.money < price:
            self.is_bankrupt = True
        else:
            self.money -= price
            self.bank_obj.money += price

    def pay_rent(self, price, player_obj):
        if self.money < price:
            self.money += self.sell_immov(price - self.money)
        if self.money < price:
            self.is_bankrupt = True
        else:
            self.money -= price
            player_obj.money += price

    def buy_immov(self, num):
        self.bank_obj.get_ownerShip(num, self.name)
        self.immov.append(copy.deepcopy(self.field_obj.field_definition[num]))

    def destroy_houses(self):
        for h in self.immov:
            h.house_amount = 0
            self.field_obj.field_definition[h.num].house_amount = 0