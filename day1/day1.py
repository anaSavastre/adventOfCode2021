def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list.append(int(line))
    return list

def firstStar(input):
    '''
    Return the number of times depth measurements increased

    input[i] > input[i-1]
    '''

    resultCount =0
    for i in range(1, len(input)):
        if input[i]>input[i-1]:
            resultCount+=1
    
    return resultCount
        
def secondStar(input):

    resultCount =0 
    prevWindow = sum(input[0:3])
    resultCount =0

    for i in range(1, len(input)-2):
        currentWindow = sum(input[i:i+3])
        if currentWindow > prevWindow:
            resultCount+=1
        prevWindow = currentWindow
    return resultCount



if __name__ =="__main__":
    # Example Input 
    testInput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    # Source Input
    sourceIn = readFile("input.txt")
    
    # STAR 1
    star01 = firstStar(sourceIn)
    print ("PART 1: ", star01)

    # STAR 2
    star02 = secondStar(sourceIn)
    print ("PART 2: ", star02)