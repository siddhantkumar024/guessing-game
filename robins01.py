import random

randomnumber = random.randint(1, 100)
print('compiler-',randomnumber)
userguess = None
guesses = 0
l = 0
s = 100
while (userguess != randomnumber):

    userguess = int(input('Enter the guess-'))
    guesses += 1
    print(f'Guess {guesses}:', userguess)

    if (userguess== randomnumber):
        print(' Right number')
        print('\n')

    else:
        if (userguess > randomnumber):

            s=userguess
            print('Try Again! You guessed too high')
            print('New range-:',l,'-',s)
            print('\n')

        else:

            l=userguess
            print('Try Again! You guessed too low')
            print('New range-:',l,'-',s)
            print('\n')
print(f"You Guessed the number in {guesses} guesses")


'''
output be like this


(compiler- 97
Enter the guess-100
Guess 1: 100
Try Again! You guessed too high
New range-: 0 - 100


Enter the guess-80
Guess 2: 80
Try Again! You guessed too low
New range-: 80 - 100


Enter the guess-85
Guess 3: 85
Try Again! You guessed too low
New range-: 85 - 100


Enter the guess-95
Guess 4: 95
Try Again! You guessed too low
New range-: 95 - 100


Enter the guess-97
Guess 5: 97
Right number)
'''
