import random

guesses = 0

print("Hello, What is your name?")
player_name = input()

hidden_number = random.randint(0,100)
print("Well, " + player_name + ', I am thinking of a number between 0 and 100. You get 10 guesses')

while guesses <10:
    print('Take a guess')
    guess = int(input())

    guesses = guesses + 1

    if guess < hidden_number:
        print('Nope, too low')
    if guess > hidden_number:
        print('Sorry, too high')
    if guess == hidden_number:
        break
if guess == hidden_number:
    guesses = str(guesses)
    print('Congrats ' + player_name + '! You got it right in ' + guesses + 'guesses!')
if guess != hidden_number:
    hidden_number = str(hidden_number)
    print('Too slow! My number was ' + hidden_number)
