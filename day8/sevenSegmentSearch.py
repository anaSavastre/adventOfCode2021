class inputData():
    def __init__(self, uniquePatter=[], output=[]):
        self.uniquePatter = uniquePatter
        self.output = output
 
def readFile(inFile):
    numbers=[]
    inData=[]
    with open(inFile, 'r') as file:
        for i, line in enumerate(file):
            splitLine = [elem.split(" ") for elem in line.replace("\n", "").split(" | ")]
            inData.append(inputData(splitLine[0], splitLine[1]))
                
    return inData

def firstStar(inData):
    """
    Count 1, 4, 7, 8 in output values
    1 -> 2 segments, 
    4 -> 4 segments, 
    7 -> 3 segments, 
    8 -> 7 segments
    """
    
    segmentLengths = [2, 4, 3, 7]
    count=0
    for elem in inData:
        for out in elem.output:
            if (len(out) in segmentLengths):
                count += 1
    return count

         
class clockMaping():
    def diff(li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif
 
    def __init__(self, inData, outData):
        self.digitMaping = {1:{'z0', 'z1'},
                            7:{'x0', 'z0', 'z1'},
                            4:{'y0', 'x1', 'z0', 'z1'},
                            8:{'x0', 'x1', 'x2', 'y0', 'y1', 'z0', 'z1'}, 
                            2:{'x0', 'x1', 'x2', 'z0', 'y1'},
                            3:{'x0', 'x1', 'x2', 'z0', 'z1'},
                            5:{'x0', 'x1', 'x2', 'y0', 'z1'},
                            0:{'x0', 'x2', 'y0', 'y1', 'z0', 'z1'}, 
                            6:{'x0', 'x1', 'x2', 'y0', 'y1', 'z1'}, 
                            9:{'x0', 'x1', 'x2', 'y0', 'z0', 'z1'}
                            }
        self.digitLength = {2:1, 3:7, 4:4, 7:8, 5:[2, 3, 5], 6:[0, 6, 9]}
        
        self.gridMaping = {'x0':[], 'x1':[], 'x2':[], 'y0':[], 'y1':[], 'z0':[], 'z1':[]}
        self.mappedLetters =set()
        self.entry = self.sortInput(self.sort(inData))
        
        self.decodeEntry()
        self.output = outData    
    
    def sort(self, list):
        sortedL = [list[0]]
        for elem in list[1:]:
            if len(elem) < len(sortedL[-1]):
                for i, sortedElem in enumerate(sortedL):
                    if len(elem) < len(sortedElem):
                        sortedL.insert(i, elem)
                        break
            else:
                sortedL.append(elem)
        return sortedL
    def sortInput(self, list):
        sorted = [[], [], []]
        segmentLengths = [2, 4, 3, 7]
        for elem in list:
            if len(elem) in segmentLengths:
                sorted[0].append(elem)
            elif len(elem) == 5:
                sorted[1].append(elem)
            elif len(elem) == 6:
                sorted[2].append(elem)
        return sorted
    def decodeEntry(self):
        # Look for specialCases 1, 7, 4, 8
        # FirstStage predictions
        for combination in self.entry[0]:
            digits = self.digitLength[len(combination)] 
            gridPoz = self.digitMaping[digits] 
            for poz in gridPoz:
                if len(self.gridMaping[poz]) ==0:
                    self.gridMaping[poz]=set(set(combination)-self.mappedLetters)
            for elem in set(combination)-self.mappedLetters:
                self.mappedLetters.add(elem)
            
        # Second Stage Prediction 
        # Look at the numbers that have a 5 digits (2, 3, 5)
        # And use what these have in common which is the fact that they all have x0, x1, x2
        
        combinations = self.entry[1]
        # Get common letters
        commonLetters = set(combinations[0])&set(combinations[1])&set(combinations[2])
        commonGridPoz = self.digitMaping[3]&self.digitMaping[2]&self.digitMaping[5]
        for gridPoz in commonGridPoz:
            self.gridMaping[gridPoz] = self.gridMaping[gridPoz]&commonLetters
        self.gridMaping["y0"] = self.gridMaping["y0"]-self.gridMaping["x1"]
        self.gridMaping["y1"] = self.gridMaping["y1"]-self.gridMaping["x2"]
        
        combinations = self.entry[2]
        commonLetters = set(combinations[0])&set(combinations[1])&set(combinations[2])

        self.gridMaping["z1"] = self.gridMaping["z1"]&commonLetters
        self.gridMaping["z0"] = self.gridMaping["z0"]-self.gridMaping["z1"]

        self.decodedDigits= {}
        for key, value in self.digitMaping.items():
            numberEncoded = set()
            for mapPoz in value:
                numberEncoded = numberEncoded.union(self.gridMaping[mapPoz])
            self.decodedDigits[key] = ''.join(numberEncoded)
                        
    
    def getOutput(self):
        # print(self.output)
        # print(self.digitMaping)
        # print(self.gridMaping)
        outNumb=''
        for number in self.output:
            for key, value in self.decodedDigits.items():
                if set(value) == set(number):
                    outNumb+=str(key)
        return int(outNumb)       

def secondStar(inData):
    result = 0
    for elem in inData:
        maping = clockMaping(elem.uniquePatter, elem.output)
        out = maping.getOutput()
        print("out ", out)
        result+=out
    
    return result
if __name__ =="__main__":
    # Example Input 
    inData = readFile("expIn.txt")
    # for elem in inData:
    #     print(elem.output)
    
    puzzleIn = readFile("in.txt")
    
    
    # STAR 1
    star01 = firstStar(puzzleIn)
    print ("PART 1: ", star01)
    
    # STAR 2
    star02 = secondStar(puzzleIn)
    print ("PART 2: ", star02)
    
    # maping=clockMaping(["acedgfb",  "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"])
    # maping.getOutput()