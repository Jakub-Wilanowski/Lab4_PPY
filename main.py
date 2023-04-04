import math


def floor(roomLength, roomWidth, panelLength, panelWidth, numInPack):
    roomArea = (roomLength * roomWidth) * 1.1
    panelArea = panelLength * panelWidth
    numOfPanels = math.ceil(roomArea / panelArea)
    numOfPacks = math.ceil(numOfPanels / numInPack)
    return numOfPacks

def primeNum(*numToCheck):
    for i in numToCheck:
        flag = True
        if(i == 0 or i == 1):
            print(str(i) + "False")
            flag = False
        else:
            for j in range(2, int(math.sqrt(i)+1)):
                if(i % j == 0):
                    print(str(i) + "False")
                    flag = False
                    break

        if(flag):
             print(str(i) + "True")


def cesarCipher(data = "", stepAmount = 0):
    temptext = data.lower()
    code = list(temptext)
    for i in range(0, stepAmount):
        temp = 0
        for j in code:

            if(ord(j)>=ord('a') and ord(j)<=ord("z")):
                print("flag1")
                j = chr(ord(j)+1)
                code[temp] = j


                if(ord(j) == ord('z')+1):
                    j = 'a'
                    code[temp] = j
            temp = temp+1
    return ''.join(code)





primeNum(1,2,5,6,9,17,18)
print(cesarCipher(data="The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", stepAmount=5))