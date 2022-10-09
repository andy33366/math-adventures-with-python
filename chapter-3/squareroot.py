def average(num1, num2):
    return (float(num1) + float(num2))/2

#finds square root using "guessing"
def squareRoot(num):

    guess = ''

    #there is currently no way in math to prove a number is a perfect square
    #so i will use user inputs

    while guess != num:
        
        lowGuess = input('low guess?')
        if lowGuess == 'stop':
           break
        highGuess = input('high guess?')
        if highGuess == 'stop':
            break
        guess = average(lowGuess, highGuess)
        if guess**2 < num:
            print('too low. guess higher')
        elif guess**2 > num:
            print('too high. guess lower')
        else:
            print(guess)
            break

    
