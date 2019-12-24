import stddraw
from transformer import *
from picture import Picture
from color import Color

class card:
    N = 700
    const = 300

    def __init__(self, num, name, coordinates, center):
        self.num = num
        self.name = name
        self.coordinates = coordinates
        self.center = center

    def draw(self, board):
        for i in range(self.coordinates[0][0], self.coordinates[0][1]):
            for j in range(self.coordinates[1][0], self.coordinates[1][1]):
                stddraw.setPenColor(board.get(j, i))
                stddraw._pixel(i + self.const , j)