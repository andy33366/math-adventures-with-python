
numList = []

def getInput():

    usInput = '.'

    while (usInput != 'stop'):
    
        print('add a number to be averaged or type stop to finalize the list')
        usInput = input()
    
        try:
            num = float(usInput)
            numList.append(num)
        except:
            if usInput == 'stop':
                print(numList)
                return
            print("type a number or the word stop")
    

def average(l):

    listLength = len(l)

    currSum = 0

    for i in l:
        currSum += i
        
    return (currSum/listLength)

getInput()

theAver = average(numList)

print('the average of the numbers provided is '+ str(theAver))
