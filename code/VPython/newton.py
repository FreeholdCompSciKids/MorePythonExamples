from visual import *



start = sphere ( pos = (0,0,0), radius = 1, color = color.white)

b1 = sphere ( pos = (0,0,0), radius = 1, color = color.green)
b2 = sphere ( pos = (10,0,0), radius = 1, color = color.red)

end = sphere ( pos = (30,0,0), radius = 1, color = color.white)


d = vector(0.5,0,0)

while true:

    while b1.pos != b2.pos:
        rate(20)
        b1.pos += d

    while b2.pos != end.pos:
        rate(20)
        b2.pos += d

    d = -1 * d

    while b2.pos != b1.pos:
        rate(20)
        b2.pos += d

    while b1.pos != start.pos:
        rate(20)
        b1.pos += d

    d = -1 * d
