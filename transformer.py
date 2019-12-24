from picture import Picture
from color import Color

def transform(c1, w, h):
    pic1 = c1
    pic2 = Picture(w, h)

    for tCol in range(w):
        for tRow in range(h):
            sCol = tCol * pic1.width() // w
            sRow = tRow * pic1.height() // h
            pic2.set(tCol, tRow, pic1.get(sCol, sRow))

    return pic2