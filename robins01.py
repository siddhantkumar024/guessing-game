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