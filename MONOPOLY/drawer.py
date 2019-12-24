import stddraw
from picture import Picture
from color import Color

class drawer:
    def __init__(self):
        stddraw.setCanvasSize(1300, 690)
        stddraw.setXscale(1,1300)
        stddraw.setYscale(1,700)

    def draw_message(self, pl, act):
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.filledRectangle(550, 250, 300, 200)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(16)
        stddraw.text(700, 350, "Player " + pl)
        print("Player " + pl + " " + act)
        stddraw.text(700, 300, act)
        stddraw.show(1500)