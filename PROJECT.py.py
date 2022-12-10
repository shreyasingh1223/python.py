
import random
print('************** GUESSSING GAME **************')
print()
while True:
    start=int(input('ENTER STARTING RANGE:  '))
    end=int(input('ENTER ENDING RANGE: '))

    score=0
    n=int(input('Enter number of times you want to try your luck: '))
    for i in range(n):
        a=random.randint(start,end)
        guess=int(input('Guess the number: '))
        if a==guess:
            print('Congrats!! You guessed the right number')
            score=score+1
        elif a>guess:
            print('Have one more try, Your guess was too low')
        elif a<guess:
            print('Have one more try, Your guess was too high')
    print()
    if score==0:
        print('Your score is: ',score)
        print('BETTER LUCK NEXT TIME')
    else:
        print('Your score is: ',score)
    print()
    
    choice=input('Do you want to play again?????(Y/N): ')
    if choice=='y' or choice=='Y':
        continue
    else:
        break




















# if score==n:
#     print('BRAVO!! YOUR GUESSING GAME IS TOO GOOD')
# if (n/2)<=score<=(n-1):
#     print('NOT THAT BAD :)')
# if score<(n/2):
#     print('YOUR GUESSING GAME IS BAD :(')
