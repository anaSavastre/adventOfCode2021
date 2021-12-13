def readFile(inFile):
    numbers=[]
    bingoBoards=[]
    with open(inFile, 'r') as file:
        for i, line in enumerate(file):
            if i==0:
                numbers = [int(elem) for elem in line.split(",")]
            else:
                if line=="\n":
                    if "bingoBoard" in locals():
                        bingoBoards.append(bingoBoard) 
                    bingoBoard=[]
                else:
                    bingoBoard.append([int(elem) for elem in line.split(" ") if elem !=""])
    bingoBoards.append(bingoBoard)
    return numbers, bingoBoards

class bingoBoard():
    def __init__(self, board):
        self.board = board
        self.numColumns = len(board[0])
        self.numRows = len(board)

        self.rows = [elem for elem in board]
        self.columns = [[board[i][j] for i in range(self.numRows)]for j in range(self.numColumns)]

        self.elements = [board[i][j] for i in range(self.numRows) for j in range(self.numColumns)]
        self.unmarkedSum = sum(self.elements)
        self.bingo = False

        self.markedRows = [0 for i in range(self.numRows)]
        self.markedColumns = [0 for i in range(self.numColumns)]

        

def firstStar(input, inBoards):
    # Create a list will all the lines for each board
    boardW = 5 
    bingoB = [bingoBoard(board) for board in inBoards]
    
    for value in input:
        for bb in bingoB:
            if value in bb.elements:
                index = bb.elements.index(value)
                bb.unmarkedSum -= value

                rowIndex = index//boardW
                colIndex = index%boardW
                # Mark row and column
                bb.markedRows[rowIndex]+=1
                bb.markedColumns[colIndex]+=1

                # Check if row or column is complete 
                if (bb.markedRows[rowIndex] == boardW):
                    # print bb.elements
                    return bb.rows[rowIndex], value, bb.unmarkedSum*value
                
                if (bb.markedColumns[colIndex] == boardW):
                    return bb.columns[colIndex], value, bb.unmarkedSum*value

def secondStar(input, inBoards):
    # Create a list will all the lines for each board
    boardW = 5 
    bingoB = [bingoBoard(board) for board in inBoards]
    numbOfBingos = 0
    for value in input:
        for i, bb in enumerate(bingoB):
            # Check if board hasn't won already 
            if bb.bingo==True:
                continue
            if value in bb.elements:
                index = bb.elements.index(value)
                bb.unmarkedSum -= value

                rowIndex = index//boardW
                colIndex = index%boardW
                # Mark row and column
                bb.markedRows[rowIndex]+=1
                bb.markedColumns[colIndex]+=1

                # Check if row or column is complete 
                if (bb.markedRows[rowIndex] == boardW or bb.markedColumns[colIndex] == boardW):
                    # # print bb.elements
                    # return bb.rows[rowIndex], value, bb.unmarkedSum*value
                    bb.bingo=True
                    numbOfBingos+=1
    
                # Check if last board was found
                if numbOfBingos==len(bingoB):
                    return bb.unmarkedSum * value

        
if __name__ =="__main__":
    # Example Input 
    input, boards = readFile("in.txt")
    
    # STAR 1
    bingoLine, val, starResult = firstStar(input, boards)
    print ("PART 1: ", bingoLine, val, starResult)

    # STAR 2
    star02 = secondStar(input, boards)
    print ("PART 2: ", star02)