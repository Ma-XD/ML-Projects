from field import *

class field_draw(field):
    def __init__(self, field_definition, coordinates):
        field.__init__(self, field_definition, coordinates)

    def draw_field(self):
        stddraw.clear()
        #stddraw.picture(self.image)
        for i in range(self.coordinates[0][0], self.coordinates[0][1]):
            for j in range(self.coordinates[1][0], self.coordinates[1][1]):
                stddraw.setPenColor(self.image.get(j,i))
                stddraw._pixel(i + self.const ,j)

        for i in range(0, 40):
            self.field_definition[i].draw(self.image)

        stddraw.show(1000)

    def draw_card(self, num):
        self.field_definition[num].draw(self.image)