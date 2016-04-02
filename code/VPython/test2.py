from visual import *
from math import *

p = 100

sun = sphere ( pos = (0,0,0), color = (1,1,0) ,radius = p/5, )

earth = {'speed': 1, 'distance': 100, 'size': 0.5 }               
earth['obj'] = sphere ( pos = (0,0,0), color = (0,0.2,0.7), radius = earth['size'] * p/10  )

mars = {'speed': 1.5, 'distance': 150, 'size': 0.4 }               
mars['obj'] = sphere ( pos = (0,0,0), color = (0.9,0.0,0.0), radius = mars['size'] * p / 10 )

venus = {'speed': 1.3, 'distance': 80, 'size': 0.5 }               
venus['obj'] = sphere ( pos = (0,0,0), color = (0.7,0.3,0), radius = venus['size'] * p / 10  )


planets = [ earth, mars, venus ]

for d in range(3600):
    rate(10)
    r = math.radians(-d*10) 
    for pl in planets:
        sp = pl['speed']
        dt = pl['distance']
        pl['obj'].pos = (dt * sin(sp*r), dt*cos(sp*r), 0)
        
        
