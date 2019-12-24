import stddraw
from player import *

class player_draw(player):
    def __init__(self, name, money, immov, position, is_bankrupt, mess_coor, field_obj, bank_obj):
        player.__init__(self, name, money, immov, position, is_bankrupt, mess_coor, field_obj, bank_obj)

    def draw_player_def(self):
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledRectangle(1 + self.name * 1000, 1, 300, 700)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(16)
        x = self.mess_coor[0]
        y = self.mess_coor[1]
        stddraw.text(x, y, "Player " + str(self.name + 1) + " money : " + str(self.money))
        y -= 20
        stddraw.text(x, y, "Immovables:")

        #print(len(self.immov))
        for i in self.immov:
            y -= 20
            stddraw.text(x, y, i.name + " rent " + str(i.rent))

        stddraw.picture(self.pics[self.name], self.field_obj.field_definition[self.position].center[0], self.field_obj.field_definition[self.position].center[1])
        stddraw.show(1000)