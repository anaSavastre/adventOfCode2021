import numpy as np

def readFile(inFile):

    with open(inFile, 'r') as file:
        txt = file.readlines()
        rows = len(txt)
        cols = len(txt[-1])-1
        list=np.zeros([rows, cols], dtype=int)
        for i, line in enumerate(txt):
            for j, chr in enumerate(line.replace("\n", "")):
                if chr == "v": value = 1
                elif chr == ">": value = 2
                else : value = 0
                list[i][j]= value
        
    return list

def printMap(matrix):
    print()
    for i in range(matrix.shape[0]):
        line=''
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 2:
                line += '>'
            elif matrix[i][j] ==1:
                line += "v"
            else:
                line += "."
            
        print(line)
 

def firstStar(matrix):
    print(matrix.shape[0], matrix.shape[1])
    iteration = 0
    directions = {"E" : [0, 1], "S" : [1, 0]}
    while(True):
        numberOfMoves = 0 
        iteration += 1

        for dir, value in zip('ES', [2,1]):
            iHerd, jHerd = np.where(matrix==value)
            iMove = []
            jMove = []
            for i, j in zip(iHerd, jHerd):
                i_next = (i + directions[dir][0]) % matrix.shape[0]
                j_next = (j + directions[dir][1]) % matrix.shape[1]
                if matrix[i_next][j_next] == 0:
                    iMove.append(i)
                    jMove.append(j)
                    # print(i, j, i_next, j_next)
                    numberOfMoves+=1
            # Move
            for i, j, in zip(iMove, jMove):
                i_next = (i + directions[dir][0]) % matrix.shape[0]
                j_next = (j + directions[dir][1]) % matrix.shape[1]
                matrix[i_next][j_next] = matrix[i][j]
                matrix[i][j] = 0

        # if iteration == 3:
        #     break
        if numberOfMoves == 0:
            print("PART1: ", iteration)
            break
    

if __name__ =="__main__":
    # exIn = readFile("exIn.txt")
    sourceIn = readFile("sourceIn.txt")
    printMap(sourceIn)

    firstStar(sourceIn)