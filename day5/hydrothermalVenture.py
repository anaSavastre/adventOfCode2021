def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            coord=[]
            for elem in line.split(" -> "):
                coord.append([int(value) for value in elem.split(",")]) 
            list.append(coord)
    return list

class lineStruct():
    def __init__(self, inData):
        self.x1 = inData[0][0]
        self.x2 = inData[1][0]

        self.y1 = inData[0][1]
        self.y2 = inData[1][1]

def printMatrix(matrix):
    for line in matrix:
            print([elem for elem in line])

def firstStar(inData):
    matrixW = 1000
    matrixDiagram = [[0 for x in range(matrixW)] for y in range(matrixW)]
    intersectionPoints = 0
    for index, line in enumerate(inData):
        line = lineStruct(line)
        if line.x1 == line.x2:
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2)+1):
                matrixDiagram[i][line.x1]+=1         
                if matrixDiagram[i][line.x1] == 2:
                    intersectionPoints+=1  
            # print("verticalLine:({} {}), ({} {})".format(line.x1, line.y1, line.x2, line.y2))
            # printMatrix(matrixDiagram)
        
        if line.y1 == line.y2:
            for i in range(min(line.x1, line.x2), max(line.x1, line.x2)+1):
                matrixDiagram[line.y1][i]+=1

                         
                if matrixDiagram[line.y1][i] == 2:
                    intersectionPoints+=1 
            # print("horizontalLine:({} {}), ({} {})".format(line.x1, line.y1, line.x2, line.y2))
            # printMatrix(matrixDiagram)
    
    return intersectionPoints

def secondStar(inData):
    matrixW = 1000
    matrixDiagram = [[0 for x in range(matrixW)] for y in range(matrixW)]
    intersectionPoints = 0
    for index, line in enumerate(inData):
        line = lineStruct(line)
        # Get coord coef
        xCoef = (line.x2 - line.x1)// max(abs(line.x2 - line.x1), 1) # To avoid division by 0
        yCoef = (line.y2 - line.y1)//max(abs(line.y2-line.y1), 1) # To avoid division by 0
        numbPointsOnLine = max(abs(line.x2 - line.x1), abs(line.y2 - line.y1))
        for point in range(numbPointsOnLine+1):
            matrixDiagram[line.y1 + point*yCoef][line.x1 + point*xCoef]+=1
            if matrixDiagram[line.y1 + point*yCoef][line.x1 + point*xCoef] == 2:
                intersectionPoints +=1
    # printMatrix(matrixDiagram)
    return intersectionPoints

if __name__ =="__main__":
    # Example Input 
    testInput = readFile("expIn.txt")
    # print(testInput)
    # Source Input
    sourceIn = readFile("in.txt")
    # print (sourceIn)
    
    # STAR 1
    star01 = firstStar(sourceIn)
    print ("PART 1: ", star01)

    # STAR 2
    star02 = secondStar(sourceIn)
    print ("PART 2: ", star02)
