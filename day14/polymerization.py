def readFile(inFile):
    polymerTemplate = ''
    pairIntersection = {}
    with open(inFile, 'r') as file:        
        for i, line in enumerate(file):
            line = line.replace("\n", "")
            if i==0:
                polymerTemplate = line
            elif line!="":
                splitLine = line.split(" -> ")
                pairIntersection[splitLine[0]] = splitLine[1]
    return polymerTemplate, pairIntersection
# AKA - brute force
def firstStar(template, pairIntersection, iterations):
    
    for i in range(iterations):    
        newTemplate = template[0]
        for i in range(len(template)-1):
            key = template[i:i+2]
            newTemplate += pairIntersection[key] + key[1]
        template = newTemplate
    occurrences = []
    for chr in set(template):
        occurrences.append(template.count(chr))
    print(occurrences)
    return max(occurrences)-min(occurrences)

# SECOND PART
def countCharacterApparitions(stringDict={}, firstElem='N'):
    occurrences = {}
    for key in stringDict.keys():
        if key[1] not in occurrences:
            occurrences[key[1]] = 0
        occurrences[key[1]] += stringDict[key]
    # Add first element
    occurrences[firstElem]+=1
    return occurrences

def secondStar(template, pairIntersection, iterations):
    string = {pair : 0  for pair in pairIntersection.keys()}
    # Initialise
    for i in range(len(template)-1):
        key = template[i:i+2]
        string[key] +=1
    
    for iter in range(iterations):
        newString = {pair : 0  for pair in pairIntersection.keys()}
        for key in string:
            if string[key] == 0:
                continue
            else:
                newChr = pairIntersection[key]
                stringCount = string[key]
                # Increment new keys
                newString[key[0]+newChr] += string[key]
                newString[newChr+key[1]] += string[key]
        string=newString
    count = countCharacterApparitions(string, template[0])
    return max(count.values())-min(count.values())
                
        
if __name__ =="__main__":
    # Example Input 
    expTemplate, expRules = readFile("expIn.txt")

    # Source Input
    srcTemplate, srcRules = readFile("in.txt")
    
    # STAR 1
    star01 = firstStar(srcTemplate, srcRules, 10)
    print ("PART 1: ", star01)

    # # STAR 2
    star02 = secondStar(srcTemplate, srcRules, 40)
    print ("PART 2: ", star02)