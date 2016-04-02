from visual import *
from random import *

WORLD_RANGE = 25

scene.autoscale = false
scene.range = WORLD_RANGE + 5

b = sphere ( pos = (1,2,0), radius = 1, color = color.yellow)
s = sphere ( pos = (0,5,0), radius = 1, color = color.red)

vx = vector(1,0,0)  #direction right 
vy = vector(0,1,0)  #direction up
vz = vector(0,0,1)  #direction fron

speed = 1

def createRings():
    for i in range(10):
        x = randint(-WORLD_RANGE, WORLD_RANGE)
        y = randint(-WORLD_RANGE, WORLD_RANGE)
        z = randint(-WORLD_RANGE, WORLD_RANGE)

        clr = choice ( [color.green, color.blue, color.cyan] ) 
        ax = choice ([vx, vy, vz])
        ring( pos = (x,y,z),
              axis = ax,
              radius = 2,
              color = color.cyan)

def move( obj, key):
    if key == 'right':
        obj.pos += vx * speed
    elif key == 'left':
        obj.pos -= vx * speed
    elif key == 'up':
        obj.pos += vy * speed
    elif key == 'down':
        obj.pos -= vy * speed
    elif key == 'f':
        obj.pos += vz * speed
    elif key == 'b':
        obj.pos -= vz * speed    
    else:
        pass

createRings()

done = false
while ( done == false ):
    key = scene.kb.getkey()
    
    if key == "esc":
        done = true
    elif key == "=":  # '+' key reports as '='
        speed *= 2
    elif key == "-":
        speed /= 2.0
    else:
        move(s, key) #move the ball s in direction given by the key

    print key


print "all done"
