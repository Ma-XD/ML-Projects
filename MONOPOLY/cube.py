import stddraw
import transformer
import random
from picture import Picture
from color import Color

class cube:
    cube_t = ["Cube1.jpg","Cube2.jpg","Cube3.jpg","Cube4.jpg","Cube5.jpg","Cube6.jpg"]
    images = []
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        for i in self.cube_t:
            self.images.append(transformer.transform(Picture(i), 20, 20))

    def get_con(self):
        cube1 = random.randrange(1, 7)
        return cube1

    def draw(self, num):
        stddraw.picture(self.images[num], self.posX, self.posY)