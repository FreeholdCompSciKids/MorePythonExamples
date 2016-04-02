from visual import *

#scene.autoscale = false
#scene.range = 10

b = sphere ( pos = (0,0,0), radius = 1, color = color.yellow)
s = sphere ( pos = (0,5,0), radius = 1, color = color.red)


vx = vector(1,0,0)
vy = vector(0,1,0)
vz = vector(0,0,1)

speed = 1

def move(key):
    if key == 'up':
      s.pos += vy * speed
    elif key == 'down':
      s.pos -= vy * speed
    elif key == 'right':
      s.pos += vx * speed
    elif key == 'left':
      s.pos -= vx * speed
    else:
      pass

done = false
while( not done):
    rate(20)
    key  = scene.kb.getkey()
    done = (key == ' ')
    move(key)

    
   
print "all done"
