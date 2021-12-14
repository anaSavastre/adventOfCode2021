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

def compatibleNeighbors(matrix, i, j, markedList):
    def checkInMarked(i, j):
        poz = [i, j] 
        if  poz not in markedList:
            return True
        return False
    returnPositions = []
    m = len(matrix)
    n = len(matrix[0])
    if (j>0 and matrix[i][j-1]!=9 and checkInMarked(i, j-1)):        
        returnPositions.append([i, j-1])
        
    if (j<n-1 and matrix[i][j+1]!=9 and  checkInMarked(i, j+1)):
        returnPositions.append([i, j+1])
        
    if (i>0 and matrix[i-1][j]!=9 and checkInMarked(i-1, j)):
        returnPositions.append([i-1, j])    
        
    if (i<m-1 and matrix[i+1][j]!=9 and checkInMarked(i+1, j)):
        returnPositions.append([i+1, j])
    
    return returnPositions

def getBasinLength(matrix, i, j, marked=[]):
    marked.append([i, j])
    neighbors = compatibleNeighbors(matrix, i, j, marked)
    while len(neighbors)>0:
             
        newN = compatibleNeighbors(matrix, neighbors[0][0], neighbors[0][1], marked)
        if neighbors[0] not in marked:
            marked.append(neighbors[0])
        
        neighbors.pop(0)
        if len(newN)>0:
            neighbors+=newN
    return len(marked)

def secondStar(inData):
    length = []
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
                basinLen = getBasinLength(inData, i, j, []) 
                length.append(basinLen)
    
    length.sort()
    return length[-3]*length[-2]*length[-1]

if __name__ =="__main__":
    # Example Input 
    testInput = readFile("inExp.txt")
    # Source Input
    sourceIn = readFile("in.txt")
    
    # # STAR 1
    # star01 = firstStar(sourceIn)
    # print ("PART 1: ", star01)


    # # STAR 2
    star02 = secondStar(sourceIn)
    print ("PART 2: ", star02)