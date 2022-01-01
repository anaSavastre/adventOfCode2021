import numpy as np

def readFile(inFile):
    
    with open(inFile, 'r') as file:
        txt = file.read().split("\n")

        # Enhancement algorithm 
        enhAlgorithm = np.zeros(len(txt[0]), dtype=int)
        for i, chr in enumerate(txt[0]):
            if chr == "#":
                enhAlgorithm[i] = 1
        txt.pop(0)
        txt.pop(0)
        inImage = np.zeros([len(txt), len(txt[0])], dtype=int)
        for i in range(len(txt)):
            for j in range(len(txt[0])):
                if (txt[i][j] == "#"):
                    inImage[i][j] = 1
    return enhAlgorithm, inImage

def expandImage(inImg):
    newRow = np.zeros([1, inImg.shape[1]], dtype=int)
    newCol = np.zeros([inImg.shape[0]+2, 1], dtype=int)
    inImg = np.vstack((np.vstack((newRow, inImg)), newRow))
    inImg = np.hstack((np.hstack((newCol, inImg)), newCol))

    return inImg

def enhancement (inImg, enhAlgorithm, iteration):
    inImg = expandImage(inImg)
    enhancedImg = np.zeros([inImg.shape[0], inImg.shape[1]], dtype=int)
    for i in range(0, inImg.shape[0]):
        for j in range(0, inImg.shape[1]):
            binaryNumber = 0
            for iOfset in range(-1, 2):
                for jOfsest in range(-1, 2):
                    binaryNumber = binaryNumber << 1
                    if (0<=i+iOfset<inImg.shape[0] and 0<=j+jOfsest<inImg.shape[1]):
                        binaryNumber = binaryNumber | inImg[i+iOfset][j+jOfsest]
                    # elif not iteration%2:
                    #     binaryNumber = binaryNumber | enhAlgorithm[-1]
                    
            # if binaryNumber == 0 and (i==0 or i==inImg.shape[0]-1 or j==0 or j==inImg.shape[1]-1):
            #     enhancedImg[i][j] = 0
            # else:
            enhancedImg[i][j] = enhAlgorithm[binaryNumber]
    rows, columns = np.where(enhancedImg ==1)
    # minI = min(rows)      
    # maxI = max(rows)
    # minJ = min(columns)      
    # maxJ = max(columns)      
    return enhancedImg
def printImage(inImage):
    print()
    for i in range(inImage.shape[0]):
        line=''
        for j in range(inImage.shape[1]):
            if inImage[i][j] == 1:
                line += '#'
            else:
                line += "."
            
        print(line)
def firstStar(inImg, enhAlgorithm):
    # inImg = expandImage(inImg)
    # printImage(inImg)

    for i in range(2):
        inImg = enhancement(np.copy(inImg), enhAlgorithm, i)
    printImage(inImg)

    nonZerElem, j = np.where(inImg!=0)
    print("PART1: ", len(nonZerElem))
    


if __name__ =="__main__":
    testAlgorithm, testIn = readFile("testIn.txt")

    sourceAlgorithm, sourceIn = readFile("sourceIn.txt")

    # PART 1
    firstStar(testIn, testAlgorithm)
    # firstStar(sourceIn, sourceAlgorithm)