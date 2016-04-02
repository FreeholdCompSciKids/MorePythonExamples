
from visual import *


def isClose(b1, b2):
    return mag( b1.pos - b2.pos) < 0.001

#SET UP CODE
b_start = sphere ( pos = (0,0,0), radius = 1, color = color.yellow)
b_end   = sphere ( pos = (50,0,0),  radius = 1, color = color.cyan)


b1 = sphere ( pos = (10,0,0) ,   radius = 1, color = color.red)
b2 = sphere ( pos = (25,0,0) ,   radius = 1, color = color.green)

d = vector(1,0,0)  #direction for b1 to move in

s1 = 1  # speed for ball 2, 0 is stop
s2 = 0  # speed for ball 2, 0 is stop 

# CODE TO MOVE STUFF

while true:
    for i in range(50):
        if (    isClose(b1,b_start)
             or isClose(b1,b_end)
             or isClose(b2,b_start)
             or isClose (b2, b_end) ):
            d *= -1 #reverse direction

        if isClose(b1,b2):
            s_temp = s1
            s1 = s2
            s2 = s_temp
 
        #move the calls        
        b1.pos += d * s1
        b2.pos += d * s2
    
        rate(10)

 

