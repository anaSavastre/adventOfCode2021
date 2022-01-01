import math

class vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
def binamialEquation(c):
    '''
    Sum(1 to x) = c =>  x(x+1)/2 = c 
    => x*x + x -2*c = 0
    '''
    delta = 1 + 8*(c)
    return (-1 + math.sqrt(delta))//2

def findXIntervals(x0, x1):
    xmin = binamialEquation(x0)
    xmax = x1
    return int(xmin)+1, xmax

def findYIntervals(y0, y1):
    return y0, abs(y0)-1

def simulation(pointPosition=vec2(0, 0), velocity=vec2(0, 0), min=vec2(0, 0), max=vec2(0, 0)):
   
    while(1):
        pointPosition.x += velocity.x
        pointPosition.y += velocity.y
        velocity.x = (velocity.x - velocity.x//abs(velocity.x)) if velocity.x !=0 else 0
        velocity.y -= 1
        if (pointPosition.x >= min.x) and (pointPosition.x <= max.x) and (pointPosition.y >= min.y) and (pointPosition.y <= max.y):
            return True
        elif (pointPosition.x > max.x) or (pointPosition.y < min.y):
            return False

def findAllInitialVelocities(min=vec2(0, 0), max=vec2(0, 0)):
    xmin, xmax = findXIntervals(min.x, max.x)
    ymin, ymax = findYIntervals(min.y, max.y)
    count = 0
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):

            flag = simulation(pointPosition=vec2(0, 0), velocity=vec2(x, y), min=min, max=max)
            if flag==True:
                # print(x, y)
                count+=1

    print(count)

if __name__ =="__main__":
    # xmin = 57
    # xmax = 116
    # ymin = -198
    # ymax = -148

    min = vec2(20, -10)
    max = vec2(30, -5)

    min = vec2(57, -198)
    max = vec2(116, -148)
    
    findAllInitialVelocities(min, max)

    # print(simulation(velocity=vec2(6, 8), min=min, max=max))