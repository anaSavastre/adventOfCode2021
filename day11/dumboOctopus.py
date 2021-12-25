import numpy as np

def readFile(inFile):
    list=np.empty([10, 10], dtype=int)
    with open(inFile, 'r') as file:
        for i, line in enumerate(file):
            for j, chr in enumerate(line.replace("\n", "")):
                list[i][j] = int(chr)

    return list

def firstStar(matrix):
    print(matrix)
    answer = 0

    for iterations in range(100):
            
        # First Step is to add one to all elements of the matrix 
        matrix+=1
        
        rowIndex, colIndex = np.where(matrix>=10)
        
        answer+=rowIndex.size
        while rowIndex.size > 0:
            i = rowIndex[0]
            j = colIndex[0]
            matrix[i][j] = 0
            for iOfs in range(-1, 2):
                for jOfs in range(-1, 2):
                    if (0<=i+iOfs<matrix.shape[0]) and (0<=j+jOfs<matrix.shape[1]):    
                        if matrix[i+iOfs][j+jOfs]!=0:
                            matrix[i+iOfs][j+jOfs] += 1 
                        if matrix[i+iOfs][j+jOfs] ==10:
                            rowIndex = np.append(rowIndex, i+iOfs)
                            colIndex = np.append(colIndex, j+jOfs)
                            answer+=1
            rowIndex = np.delete(rowIndex, 0)
            colIndex = np.delete(colIndex, 0)
            
        

    print("PART 1: ", answer)

def secondStar(matrix):
    
    iterations = 0
    # for iterations in range(200):
    while(True):
        iterations+=1
            
        # First Step is to add one to all elements of the matrix 
        matrix+=1
        
        rowIndex, colIndex = np.where(matrix>=10)

        flashes=rowIndex.size
        
        while rowIndex.size > 0:
            i = rowIndex[0]
            j = colIndex[0]
            matrix[i][j] = 0
            for iOfs in range(-1, 2):
                for jOfs in range(-1, 2):
                    if (0<=i+iOfs<matrix.shape[0]) and (0<=j+jOfs<matrix.shape[1]):    
                        if matrix[i+iOfs][j+jOfs]!=0:
                            matrix[i+iOfs][j+jOfs] += 1 
                        if matrix[i+iOfs][j+jOfs] ==10:
                            rowIndex = np.append(rowIndex, i+iOfs)
                            colIndex = np.append(colIndex, j+jOfs)
                            flashes+=1
            rowIndex = np.delete(rowIndex, 0)
            colIndex = np.delete(colIndex, 0)

        if np.where(matrix==0)[0].size == matrix.size:
            print(matrix)
            print("PART 2: ", iterations)
            return

if __name__ =="__main__":
    expIn = readFile("expIn.txt")
    sourceIn = readFile("in.txt")
    # star01 = firstStar(sourceIn)
    star02 = secondStar(sourceIn)