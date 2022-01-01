def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            row = [int(elem) for elem in line.replace("\n", "")]
            list.append(row)
    return list
 
def firstStar(inMatrix):
    
    def getNeighbors(index):
        i=index//width
        j=index%width
        c0 = i*width+(j+1) if j+1 < width else None
        c1 = (i+1)*width+j if i+1 < height else None
        c2 = i*width+(j-1) if j-1 > 0 else None
        c3 = (i-1)*width+j if i-1 > 0 else None
        print(i, j, c0, c1)
        return c0, c1, c2, c3 

    def assesElementCost(index, connection0):
        i=index//width
        j=index%width
        # See if current position is a compatible connection 
        if nodeCost[connection0] > nodeCost[index]+inMatrix[i][j]:
            nodeConnections[connection0] = index 
            nodeCost[connection0] = nodeCost[index]+inMatrix[i][j]
        
        if connection0 not in visited and connection0 not in visitPoz:
            visitPoz.append(connection0)
        
    # Initializing all out lists
    width = len(inMatrix[0])
    height = len(inMatrix)
    n = width*height
    # Appending the neighbors of first element
    visitPoz = [0]
    visited = []
    nodeConnections = {0:None}
    nodeCost={}
    for i in range(len(inMatrix)):
        for j in range(len(inMatrix[0])):
            nodeCost[i*width +j] = float("inf")
    nodeCost[0] = 0 
    
    while(len(visitPoz)>0):
        currentPosition = visitPoz[0]   
        
        connection0, connection1 = getNeighbors(currentPosition)
        if connection0!=None:
            assesElementCost(currentPosition, connection0)
        if connection1!=None:
            assesElementCost(currentPosition, connection1)
        
        visited.append(currentPosition)
        visitPoz.pop(0)
        

    for i in range(height):
        dict = {}
        for j in range(width):
            dict[i*width + j]=nodeCost[i*width +j]
        print(dict)
    print()
    elem = n-1
    path = []
    while elem!=None:
        path.append(elem)
        elem = nodeConnections[elem]
    path.reverse()
    print(path)
    print(len(path))
        
if __name__ =="__main__":
    # Example Input 
    testInput = readFile("inExp.txt")
    # Source Input
    sourceIn = readFile("in.txt")
    print("len source ", len(sourceIn), len(sourceIn[0]))
    # STAR 1
    star01 = firstStar(sourceIn)
    print ("PART 1: ", star01)