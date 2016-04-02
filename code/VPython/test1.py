
from visual import *


mars = sphere( pos=(1,2,1),
            color = (1,0.5,0),
            radius = 10)

venus = sphere( pos=(20,0,0),
            color = (0,0.5,1),
            radius = 10)


h = helix( pos=(10,20,),
            color = (1,0,1),
            radius = 10)

for x in range(10):
    mars.pos = (x, 0, 0)
    rate(10)
