from visual import *

def makeHat(position):
    x,y,z = position
    hatPart1 = cylinder( pos = position + vector(0,9,0),
                         axis = vector(0, 1.5, 0),
                         radius = 0.5,
                         color = color.green)

    hatBrim = cylinder( pos =  position + vector (0,9,0),
                         axis = (0, 0.2, 0),
                         radius = 1.5,
                         color = color.green)
    
def makeSnowMan(position):
    print position

    x, y, z = position
    
    bigBall = sphere( pos = position + vector(0,0,0),
                      radius = 3,
                      color = color.white )

    mediumBall = sphere( pos = position + vector(0,5,0),
                      radius = 2,
                      color = color.white )

    smallBall = sphere( pos = position + vector(0,8,0),
                      radius = 1,
                      color = color.white )

    makeHat(position)    

def makeRowOfSnowMen(y,z):
    x = 0
    for i in range(8):
        x = x + 5
        makeSnowMan( position = vector(x,y,z) )

def makeSquareOfSnowMen(y):
    z=0        
    for i in range(6):
        makeRowOfSnowMen(y,z)
        z += 5

def makeCubeOfSnowMen():
    y = 0
    for i in range(2):
        makeSquareOfSnowMen(y)
        y += 15

def makeFloor():
    pass    


#============================================


def main():
    makeRowOfSnowMen(0,0)
        
if __name__ == "__main__":
    main()
