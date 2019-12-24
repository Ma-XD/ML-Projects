class bank:
    def __init__(self, money, field_obj):
        self.money = money
        self.field_obj = field_obj

    def get_ownerShip(self, immov_num, player):
        self.money += self.field_obj.field_definition[immov_num].price
        self.field_obj.field_definition[immov_num].owner = player
        return True

    def buy_immovable(self, immov_price, immov_num):
        self.money -= int(immov_price/5)
        self.field_obj.field_definition[immov_num].owner = "bank"
        self.field_obj.field_definition[immov_num].house_amount = 0
        return int(immov_price/5)