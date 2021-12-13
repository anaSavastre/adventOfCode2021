def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list.append(int(line))
    return list

def lanternFishSpawn(days):

    fishList = [0]
    fishPerDay = {}
    for day in range(days):
        if day-days<=7:
            fishPerDay[day] = [elem for elem in fishList]
        for i in range(len(fishList)):
            if fishList[i] == 0:
                fishList[i] = 6
                fishList.append(8)
            else:
                fishList[i] -= 1
        # print(fishList)
    # print(fishPerDay)
    return fishPerDay

def fishSpawnOptimized(days):
    fishList = [0]
    fishPerDay = {}
    for day in range(days):
        if days-day<=7:
            fishPerDay[day] = len(fishList)
        for i in range(len(fishList)):
            if fishList[i] == 0:
                fishList[i] = 6
                fishList.append(8)
            else:
                fishList[i] -= 1
        # print(fishList)
    # print(fishPerDay)
    return fishPerDay

def firstStar(inData, numbDays):
    fishCycle = lanternFishSpawn(numbDays)
    sum=0
    for cycleOffs in inData:
        sum+=len(fishCycle[numbDays-cycleOffs])
    return sum


# SECOND STAR 

class lanternFish():
    def __init__(self, life=0, count=0):
        self.life = life
        self.count = count
       

def respMatrixSum(m):
    sum=0
    for elem in m:
        sum += elem[1]
    return sum

def respawn(numbDays, inData):
    respawnMatrix = [[0, 0] for elem in range(8)] 
    respawnMatrix[0] = [1, 1]
    sumList = {}
   
    # Respwn Simulation
    for day in range(numbDays):
        index = day%7
        respwnFishIndex=(index + 2)%7
        respawnMatrix[respwnFishIndex][0] = respawnMatrix[respwnFishIndex][1]
        respawnMatrix[respwnFishIndex][1] += respawnMatrix[index][0] 
        
        if numbDays-day<=7:
            sumList[numbDays-day-1] = respMatrixSum(respawnMatrix)
    
    # Counting numb of fish for the given inData
    count = 0    
    for cycleOffs in inData:
        count+=sumList[cycleOffs]

    return count

        



if __name__ =="__main__":
   
    # Example Input 
    testInput = [3,4,3,1,2]

    # Source Input
    sourceIn = [1,4,1,1,1,1,5,1,1,5,1,4,2,5,1,2,3,1,1,1,1,5,4,2,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,4,1,1,1,1,4,1,1,5,5,1,1,1,4,1,1,1,1,1,3,2,1,1,1,1,1,2,3,1,1,2,1,1,1,3,1,1,1,2,1,2,1,1,2,1,1,3,1,1,1,3,3,5,1,4,1,1,5,1,1,4,1,5,3,3,5,1,1,1,4,1,1,1,1,1,1,5,5,1,1,4,1,2,1,1,1,1,2,2,2,1,1,2,2,4,1,1,1,1,3,1,2,3,4,1,1,1,4,4,1,1,1,1,1,1,1,4,2,5,2,1,1,4,1,1,5,1,1,5,1,5,5,1,3,5,1,1,5,1,1,2,2,1,1,1,1,1,1,1,4,3,1,1,4,1,4,1,1,1,1,4,1,4,4,4,3,1,1,3,2,1,1,1,1,1,1,1,4,1,3,1,1,1,1,1,1,1,5,2,4,2,1,4,4,1,5,1,1,3,1,3,1,1,1,1,1,4,2,3,2,1,1,2,1,5,2,1,1,4,1,4,1,1,1,4,4,1,1,1,1,1,1,4,1,1,1,2,1,1,2]
    
    resp = respawn(256, sourceIn)
    print(resp)
  