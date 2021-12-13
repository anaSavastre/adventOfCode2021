def readFile(inFile):
    dots=[]
    folds = []
    with open(inFile, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            if "y" in line or "x" in line:
                line = line.replace("fold along ", "")
                splitted = line.split("=")
                folds.append(foldStruct(splitted[0], int(splitted[1])))
                
            elif line != "":
                pt = [int(elem) for elem in line.split(",")]
                dots.append(pointStruct(pt))
    return dots, folds

class pointStruct():
    def __init__(self, xy=[]):
        self.x=xy[0]
        self.y=xy[1]
class foldStruct():
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value
class paper():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for y in range(height)]

def output(paper):
    out = open("out.txt", "w")
    for row in paper:
        for point in row:
            out.write(" " if point == 0 else "#")
        out.write("\n")
    
def foldY(trnPaper, foldValue):
    n = trnPaper.height
    y=foldValue
    k = max(y, n-y-1)        
    foldedPaper = paper(trnPaper.width, k)
    for i in range(k):
        for pointIndex in range(trnPaper.width):
            upperPoint = trnPaper.grid[i][pointIndex] 
            lowerPoint = trnPaper.grid[n-i-1][pointIndex]
            foldedPaper.grid[i][pointIndex] = upperPoint or lowerPoint
    # output(foldedPaper.grid)   
    return foldedPaper    

def foldX(trnPaper, x):
    n=trnPaper.width
    k = max(x, n-x-1)
    foldedPaper = paper(k, trnPaper.height)
    for i in range(k):
        for pointIndex in range(trnPaper.height):
            upperPoint = trnPaper.grid[pointIndex][i] 
            lowerPoint = trnPaper.grid[pointIndex][n-i-1]
            foldedPaper.grid[pointIndex][i] = upperPoint or lowerPoint
    return foldedPaper


def firstStar(points, fold):
    
    width = max([elem.x for elem in points])+1
    height = max([elem.y for elem in points])+1
    print(height, width)
    # Create transparentPaper
    transparentPaper = paper(width, height)
    # Populate paper with points 
    for point in points:
        transparentPaper.grid[point.y][point.x] = 1
    
    if fold.axis == "y":
        foldedPaper = foldY(transparentPaper, fold.value)
    else:
        foldedPaper = foldX(transparentPaper, fold.value)
    # Count numberOfPoints
    result=0
    for row in foldedPaper.grid:
        result+=sum(row)
        
    return result        
    # foldX(folded, 5)
    
def secondStar(points, folds):
    width = max([elem.x for elem in points])+1
    height = max([elem.y for elem in points])+1
    # Create transparentPaper
    transparentPaper = paper(width, height)
    # Populate paper with points 
    for point in points:
        transparentPaper.grid[point.y][point.x] = 1
        
    # Fold 
    paperToFold = transparentPaper
    for fold in folds:
        if fold.axis == "y":
            foldedPaper = foldY(paperToFold, fold.value)
        else:
            foldedPaper = foldX(paperToFold, fold.value)
        paperToFold = foldedPaper
    output(paperToFold.grid)
if __name__ =="__main__":
    dots, folds = readFile("expIn.txt")
    
    sDots, sFolds = readFile("in.txt")
    # print("input", dots)
    # print("folds", folds)
    
    # FIRST STAR 
    star01 = firstStar(sDots, sFolds[0])
    print("* First Star: ", star01 )
    
    # SECOND STAR 
    star02 = secondStar(sDots, sFolds)
    # print("** First Star: ", star01 )