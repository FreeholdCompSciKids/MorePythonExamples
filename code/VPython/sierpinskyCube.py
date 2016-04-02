from visual import *

OFFSETS=(-1,0,1)

def makeSierpinskiCube( p, a, level):
    
    if level == 1:
        box(pos=p, length=a, height=a, width=a)

    else:
        for x in OFFSETS:
            for y in OFFSETS:
                for z in OFFSETS:
                    numZero = sum( n==0 for n in [x,y,z])
                    if ( numZero < 2):
                        np = p + (a/3) * vector(x,y,z)
                        makeSierpinskiCube(np, a / 3, level -1)


if __name__ == "__main__":
    makeSierpinskiCube( vector(0,0,0), 81*81 , 2)
