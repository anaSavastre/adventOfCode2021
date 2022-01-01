def firstStar(p1Start, p2Start):
    diceValue = [elem+1 for elem in range(100)]
    circularPositions = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    diceIndex=1
    p1Score = 0
    p2Score =0
    p1Poz=p1Start
    p2Poz=p2Start
# while p1Score<1000 or p2Score<1000:

    for i in range(1000):
        
        p1Poz =(p1Poz + 3*diceIndex + 3)%10
        p1Score += circularPositions[p1Poz]
        diceIndex+=3
        if(p1Score >= 1000):
            print("winner: Player1")
            print("Result: ", p2Score, diceIndex-1)
            return p2Score*(diceIndex-1)

        p2Poz =(p2Poz + 3*diceIndex + 3)%10
        p2Score += circularPositions[p2Poz]

        # print("Player1: ", p1Poz, p1Score)
        # print("Player2: ", p2Poz, p2Score)
        diceIndex+=3

        if(p2Score >= 1000):
            print("winner: Player2")
            print("Result: ", p1Score, diceIndex-1)
            return p1Score*(diceIndex-1)

class playerScore():
    def __init__(self, start):
        self.locationCount = [0 for i in range(10)]
        self.locationCount[start]=1

        self.scoreLocations = {i:[0 for j in range(21)] for i in range(10)}
        self.scoreLocations[start][0] = 1
        self.winCount = 0
        self.circularPositions = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.universes={}
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    move = i+j+k
                    if move in self.universes.keys():
                        self.universes[move] += 1
                    else:
                        self.universes[move] =1
        print("universes", self.universes)
    
    def simulateGame(self):
        # for round in range(rounds):
        newLocCount = [0 for i in range(10)]
        newScoreLocations = {i:[0 for j in range(21)] for i in range(10)}
        for move in self.universes.keys():
            moveCount = self.universes[move]
            for location, countPerLoc in enumerate(self.locationCount):
                if countPerLoc == 0:
                    continue
                # print("location: ", location, countPerLoc)
                resultLocation = (location+move)%10 
                # print("resuntLoc: ", resultLocation)
                newLocCount[resultLocation] +=  self.locationCount[location] * moveCount

                for score, scoreCount in enumerate(self.scoreLocations[location]):
                    if scoreCount == 0:
                        continue
                    newScore = self.circularPositions[resultLocation] + score
                    if newScore >= 21 :
                        self.winCount += scoreCount
                        continue
                    newScoreLocations[resultLocation][newScore] += scoreCount

        self.locationCount = newLocCount
        self.scoreLocations = newScoreLocations
        
def secondStar(p1Start, p2Start):
    player1 = playerScore(p1Start)
    player2 = playerScore(p2Start)
       round in range(2):
        player1.simulateGame()
        # player2.simulateGame()

        print(player1.locationCount)
        print(player1.scoreLocations)
        print("player1 winds: ", player1.winCount)
        # print(player2.winCount)

        

if __name__ =="__main__":
    p1 = 4
    p2 = 8

    star00 = firstStar(p1, p2)
    print("PART 1: ", star00)

    # player1 = playerScore(p1)

    # player1.simulateGame(2)

    star02 = secondStar(p1, p2)
