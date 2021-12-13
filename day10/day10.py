def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list.append(line)
    return list

def firstStar(inData):
    openBrk='([{<'
    closedBrk=')]}>'
    illegalChrDict = {")":3, "]":57, "}":1197, ">":25137}
    illegalCost=0
    incompleteRows = []
    for row in inData:
        openStack = []
        incompRow = False
        for bracket in row:
            # print("stack", openStack)
            if bracket in openBrk:
                openStack.append(bracket)
            elif bracket in closedBrk:
                # If NOT compatible
                if openBrk.index(openStack[-1]) != closedBrk.index(bracket):
                    illegalCost+=illegalChrDict[bracket]
                    incompRow=True
                    break
                else:
                    openStack.pop(-1)
        # Memorize just the incomplete rows
        if not incompRow:
            incompleteRows.append(row)
                        
    return illegalCost, incompleteRows

def secondStar(inData):
    openBrk='([{<'
    closedBrk=')]}>'
    scores=[]
    for row in inData:
        openStack = []
        for bracket in row:
            # If Closed bracket
            if bracket in openBrk:
                openStack.append(bracket)
            elif bracket in closedBrk:
                # Assuming we have filtered the list of any incompatible brackets 
                # So we are just taking out of the stack the last element
                openStack.pop(-1)
        
        # Now we need to close all the remaning opened brackets 
        if len(openStack)>0:
            completionScore = 0
            openStack.reverse()
            
            for bracket in openStack:
                bracketPoint = openBrk.index(bracket)+1
                completionScore = completionScore*5 + bracketPoint
            scores.append(completionScore)
    scores.sort()
    return scores[len(scores)//2]
        
        

if __name__ =="__main__":
    # Example Input 
    testInput = readFile("exp.txt")
    # # Source Input
    sourceIn = readFile("in.txt")
    
    # STAR 1
    star01, filteredInData = firstStar(sourceIn)
    print ("PART 1: ", star01)
    
    # STAR 2
    star02 = secondStar(filteredInData)
    print ("PART 2: ", star02)
    