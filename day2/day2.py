def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            text = line.split(" ")
            list.append([text[0], int(text[1])])
    return list

class coordinatesStruct():
    def __init__(self, f=0, d=0, a=0):
        self.forward = f
        self.depth = d
        self.aim = a

def firstStar(input):
    coordinates = coordinatesStruct(0, 0)
    for elem in input:
        if elem[0] == "forward":
            coordinates.forward += elem[1]
        elif elem[0] == "down":
            coordinates.depth += elem[1]
        elif elem[0] == "up":
            coordinates.depth -= elem[1]
    
    return coordinates

def secondStar(input):
    coordinates = coordinatesStruct(0, 0)
    for elem in input:
        direction = elem[0]
        x = elem[1]
        if direction == "forward":
            coordinates.forward += x
            coordinates.depth += coordinates.aim * x
        elif direction == "down":
            coordinates.aim += x
        elif direction == "up":
            coordinates.aim -= x
    
    return coordinates

if __name__ =="__main__":
    # Example Input 
    testInput = readFile("exampleIn.txt")
    # Source Input
    sourceIn = readFile("input.txt")
    
    # STAR 1
    star01 = firstStar(sourceIn)
    print ("PART 1: ", star01.forward, star01.depth, "=> result is: ", star01.forward*star01.depth)

    # STAR 2
    star02 = secondStar(sourceIn)
    print ("PART 2: ", star02.forward, star02.depth, "=> result is: ", star02.forward*star02.depth)