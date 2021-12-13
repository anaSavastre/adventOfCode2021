def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            row = [int(elem) for elem in line.replace("\n", "")]
            list.append(row)
    return list


def firstStar(inData):
    count = 0
    m = len(inData)
    n = len(inData[0]) 
    for i in range(m):
        for j in range(n):
            adjLoc = []
            # Horizontal
            if j>0:
                adjLoc.append(inData[i][j-1])
            if j<n-1:
                adjLoc.append(inData[i][j+1])
            if i>0:
                adjLoc.append(inData[i-1][j])    
            if i<m-1:
                adjLoc.append(inData[i+1][j])
            
            if (inData[i][j] < min(adjLoc)):
                count += inData[i][j] + 1
    
    return count


def compatibleNeighbors(matrix, i, j):
    returnPositions = []
    m = len(matrix)
    n = len(matrix[0])
    if j>0 and matrix[i][j-1]!=9:
        returnPositions.append([i, j-1])
    if j<n-1 and matrix[i][j+1]!=9:
        returnPositions.append([i, j+1])
    if i>0 and matrix[i-1][j]!=9:
        returnPositions.append([i-1, j])    
    if i<m-1 and matrix[i+1][j]!=9:
        returnPositions.append([i+1, j])
    
    return returnPositions

def getBasin(matrix, i, j):
   neighbors = compatibleNeighbors(matrix, i, j)
   for pos in neighbors:
       print(compatibleNeighbors(matrix, pos[0], pos[1]))
#    print(neighbors)

if __name__ =="__main__":
    # Example Input 
    testInput = readFile("inExp.txt")
    # Source Input
    sourceIn = readFile("in.txt")
    
    # # STAR 1
    # star01 = firstStar(sourceIn)
    # print ("PART 1: ", star01)


    # # STAR 2
    print(testInput)
    print(getBasin(testInput, 0, 0))
    # star02 = secondStar(sourceIn)
    # print ("PART 2: ", star02)compatibleNeighbors