def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list.append(line.replace("\n", ""))
    return list

def BinaryToDecimal(num):
    expo =1
    dec_num= 0
    while(num):
        digit = num % 10
        num = int(num / 10)
        
        dec_num += digit * expo
        expo = expo * 2
    return dec_num

# PART 1 
def firstStar(input):
    gammaRate = 0
    epsilonRate = 0
    # First Element
    positionSumArray = [int(i) for i in input[0]]

    for elem in input[1:]:

        for i, decimal in enumerate(elem):
            positionSumArray[i]+=int(decimal)

    gammaDigitList = [1 if elem > len(input)/2 else 0 for elem in positionSumArray]
    
    # print(gammaDigitList)
    for gammaDigit in gammaDigitList:
        gammaRate = gammaRate*10 + gammaDigit
        epsilonRate = epsilonRate*10 + int(not gammaDigit)

    # print (BinaryToDecimal(gammaRate)*BinaryToDecimal(epsilonRate))
        
            
    return gammaRate, epsilonRate

# PART 2 
def binaryDiagnostic(input, digit, bitCriteria):
    '''
    bitCriteria =   1 -> most commont
                    0 -> least common
    '''
    if len(input)==1:
        print ("BIT DIAGNOSTIC RESULT IS: ", input[0])
        return int(input[0])

    digitSum = sum(int(elem[digit]) for elem in input)
    keepDigit = 1-(1-bitCriteria) if digitSum >= len(input)/2 else (1-bitCriteria)
    newList = [elem for elem in input if elem[digit] == str(keepDigit)]
    
    return binaryDiagnostic(newList, digit+1, bitCriteria)
    
    
    # for elem in input:

def secondStar(input):
    oxygen = binaryDiagnostic(input, 0, 1)
    co2 = binaryDiagnostic(input, 0, 0)
    print ("oxygen: {}, co2: {}".format(oxygen, co2))
    return BinaryToDecimal(oxygen)*BinaryToDecimal(co2)

if __name__ =="__main__":
    # Example Input 
    testInput = []

    # Source Input
    sourceIn = readFile("input.txt")
    # print (sourceIn)
    
    # STAR 1
    star01 = firstStar(sourceIn)
    star01Rez = BinaryToDecimal(star01[0])*BinaryToDecimal(star01[1])
    print ("PART 1: ", star01Rez)

    # # STAR 2
    star02 = secondStar(sourceIn)
    print ("PART 2: ", star02)