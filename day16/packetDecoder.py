
def convertFromHexToBinary(hex):
    conversionDict = {"A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    binary = ''
    for chr in hex:
        if chr in conversionDict.keys():
            binary+=conversionDict[chr]
        else:
            string = decimalToBinary(chr)
            binary+=string
    return binary

def decimalToBinary(n):
    binary = "000{0:b}".format(int(n))
    return binary[-4:]

def binaryToDecimal(num):
    expo =1
    dec_num= 0
    while(num):
        digit = num % 10
        num = int(num / 10)
        
        dec_num += digit * expo
        expo = expo * 2
    return dec_num


def literalValue(binaryIn, index):
    # Terminate clause
    if binaryIn[index] == "0":
        value = binaryIn[index+1:index+5]
        return value, index+5
    else:
        value = binaryIn[index+1:index+5]
        totalValue, index = literalValue(binaryIn, index+5)

        # if concatenatedBinaryIn=='':concatenatedBinaryIn=None
        
        return value+totalValue, index

def operation(typeID, values):
    if typeID == 0:
        return sum(values)
    elif typeID == 1:
        prod =1
        for elem in values:
            prod*=elem
        return prod

    elif typeID == 2:
        return min(values)
    
    elif typeID == 3:
        return max(values)
    elif typeID == 5:
        return 1 if values[0] > values[1] else 0
    elif typeID == 6:
        return 1 if values[0] < values[1] else 0
    elif typeID == 7:
        return 1 if values[0] == values[1] else 0


def recursivePackageDecoder(binaryIn, index):
    typeId = int(binaryIn[index+3:index+6], 2)
    index+=6
    values=[]
    # LITERAL VALUES
    if typeId==4:
        value, index = literalValue(binaryIn, index)
        return int(value,2), index
    else:
        operator = binaryIn[index]

        # LENGTH TYPE: 0 => total length
        if operator == '0' :
            totalLength = int(binaryIn[index+1:index+16],2)
            index+=16
            endIndex = index+totalLength
            while index < endIndex:
                value, index = recursivePackageDecoder(binaryIn, index)
                values.append(value)

        # LENGTH TYPE: 1 => number of subpackages
        else :
            numberOfPackages = int(binaryIn[index+1:index+12], 2)
            index+=12
            for i in range(numberOfPackages):
                value, index = recursivePackageDecoder(binaryIn, index)
                values.append(value)
    return operation(typeId, values), index


def partTwo(input):
    # Decode Input 
    binaryIn = convertFromHexToBinary(input)
    value = recursivePackageDecoder(binaryIn, 0)
    
    # while len(binaryIn) > 0
    return value 

   
if __name__ =="__main__":
   
    # Example Input 
    testInput00 = '9C0141080250320F1802104A08'

    pyzzleIn = 'A059141803C0008447E897180401F82F1E60D80021D11A3DC3F300470015786935BED80A5DB5002F69B4298A60FE73BE41968F48080328D00427BCD339CC7F431253838CCEFF4A943803D251B924EC283F16D400C9CDB3180213D2D542EC01092D77381A98DA89801D241705C80180960E93469801400F0A6CEA7617318732B08C67DA48C27551C00F972830052800B08550A277416401A5C913D0043D2CD125AC4B1DB50E0802059552912E9676931530046C0141007E3D4698E20008744D89509677DBF5759F38CDC594401093FC67BACDCE66B3C87380553E7127B88ECACAD96D98F8AC9E570C015C00B8E4E33AD33632938CEB4CD8C67890C01083B800E5CBDAB2BDDF65814C01299D7E34842E85801224D52DF9824D52DF981C4630047401400042E144698B2200C4328731CA6F9CBCA5FBB798021259B7B3BBC912803879CD67F6F5F78BB9CD6A77D42F1223005B8037600042E25C158FE0008747E8F50B276116C9A2730046801F29BC854A6BF4C65F64EB58DF77C018009D640086C318870A0C01D88105A0B9803310E2045C8CF3F4E7D7880484D0040001098B51DA0980021F17A3047899585004E79CE4ABD503005E610271ED4018899234B64F64588C0129EEDFD2EFBA75E0084CC659AF3457317069A509B97FB3531003254D080557A00CC8401F8791DA13080391EA39C739EFEE5394920C01098C735D51B004A7A92F6A0953D497B504F200F2BC01792FE9D64BFA739584774847CE26006A801AC05DE180184053E280104049D10111CA006300E962005A801E2007B80182007200792E00420051E400EF980192DC8471E259245100967FF7E6F2CF25DBFA8593108D342939595454802D79550C0068A72F0DC52A7D68003E99C863D5BC7A411EA37C229A86EBBC0CB802B331FDBED13BAB92080310265296AFA1EDE8AA64A0C02C9D49966195609C0594223005B80152977996D69EE7BD9CE4C1803978A7392ACE71DA448914C527FFE140'
    
    # First Star 
    star00=partTwo(pyzzleIn)
    print("PART2: ", star00)