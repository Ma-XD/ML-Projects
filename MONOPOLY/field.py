import stddraw
import transformer
from picture import Picture
from color import Color

class field:
    N = 700
    const = 300
    
    def __init__(self, field_definition, coordinates):
        self.field_definition = field_definition
        self.image = transformer.transform(Picture("board.jpg"), self.N, self.N)
        self.coordinates = coordinates

    def action(self, number):
        if self.field_definition[number].is_action:
            return self.field_definition[number].name
        else:
            return "non_action"