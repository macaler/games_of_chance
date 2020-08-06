# first we'll need the random package if we are to construct games of chance involving ... well,
# random chance. Also, we'll need the sys package in order to end the game if we go broke (or
# if we choose the "halt" option in runagame):

import random
import sys

# How many tokens you start out with.
tokens = 100
# I am changing this variable name from "money" to "tokens" so as not to give the impression that
# any real money is/was involved in the writing, creation, or running of this code. These games of
# chance are for fun only, and no actual real betting using actual real money is taking place.

# Before I do anything else, I should write a function that checks to see if the bet amount is bigger
# than the amount of tokens the player has right now:

def checkbalance(amount, betamount):
    if amount <= 0:
        print("You're broke, you can't do any more betting.")
        sys.exit()
    elif amount < betamount:
        print('That bet is for more than the tokens you have. Try again.')
        return 
    elif betamount < 0:
        print("Can't bet a negative amount. Try again.")
        return 

# First up: To create a function that simulates flipping a coin and calling either "heads" or "tails."

def flipacoin(betamount, call, amount):

    checkbalance(amount, betamount)
    if (amount < betamount or betamount < 0):
        return amount

    if betamount == 0:
        print("You gotta bet something! Make a real bet.")
        return amount

    flip_outcome = random.randint(1,2)
    outcome_label = "heads" if flip_outcome == 1 else "tails"
    
    # Let's call an outcome of 1 "heads", and an outcome of 2 "tails."

    if call == 'heads' and flip_outcome == 1:
        print('You called {} and the result of the coin flip was {}'.format(call,outcome_label))
        print('You win!')
        print('You won {} tokens.'.format(betamount))
        newtokens = amount + betamount
    elif call == 'tails' and flip_outcome == 2:
        print('You called {}, and the result of the coin flip was {}'.format(call,outcome_label))
        print('You win!')
        print('You won {} tokens.'.format(betamount))
        newtokens = amount + betamount
    elif (call == 'heads' and flip_outcome == 2) or (call == 'tails' and flip_outcome == 1):
        print('You called {}, but the result of the coin flip was {}'.format(call,outcome_label))
        print('You lose!')
        print('You lost {} tokens.'.format(betamount))
        newtokens = amount - betamount
    else:
        print("Acceptable calls are 'heads' and 'tails'.")
        print("Please try again.")
        return amount

    return newtokens

# Next up: to create a function that simulates playing the game Cho-Han, in which one bets
# on whether the sum of two rolled die will be even or odd:

def chohan(betamount, call, amount):

    checkbalance(amount, betamount)
    if (amount < betamount or betamount < 0):
        return amount

    if betamount == 0:
        print("You gotta bet something! Make a real bet.")
        return amount

    diceone = random.randint(1,6)
    dicetwo = random.randint(1,6)
    sumofdice = diceone + dicetwo

    print('Dice one rolled a {}.'.format(diceone))
    print('Dice two rolled a {}.'.format(dicetwo))
    
    if call == 'odd' and sumofdice%2 == 1:
        print('You called {} and the sum of the two dice was {}'.format(call,sumofdice))
        print('You win!')
        print('You won {} tokens.'.format(betamount))
        newtokens = amount + betamount
    elif call == 'even' and sumofdice%2 == 0:
        print('You called {}, and the sum of the two dice was {}'.format(call,sumofdice))
        print('You win!')
        print('You won {} tokens.'.format(betamount))
        newtokens = amount + betamount
    elif (call == 'odd' and sumofdice%2 == 0) or (call == 'even' and sumofdice%2 == 1):
        print('You called {}, but the sum of the two dice was {}'.format(call,sumofdice))
        print('You lose!')
        print('You lost {} tokens.'.format(betamount))
        newtokens = amount - betamount
    else:
        print("Acceptable calls are 'odd' and 'even'.")
        print("Please try again.")
        return amount

    return newtokens

# Now to write a function that simulates two players picking a card randomly from a deck of cards.
# The higher number should win, and the amount of the bet should be returned if there is a tie.
# I will think about this game in the following way: the player picks a card, and the "dealer" (like a
# dealer at a casino) picks the other card. Both picks will take place automatically, without the player
# having to type in that they picked.

def pickacard(betamount, amount):

    checkbalance(amount, betamount)
    if (amount < betamount or betamount < 0):
        return amount

    if betamount == 0:
        print("You gotta bet something! Make a real bet.")
        return amount


    print('Aces count as 1; Jacks count as 11; Queens count as 12; Kings count as 13')

    # I'm going to go with the convention that Jacks count as 11, Queens count as 12, and 
    # Kings count as 13. This isn't the standard blackjack values, but we aren't playing blackjack
    # and this convention will help lower the amount of ties. I'm also going to let aces be low 
    # and call them "1." My lab students always hated that I did this, but it let me assign students
    # to lab tables with a simple deck of playing cards. Haters gonna hate.
    # No wild cards or jokers in my simulated deck of cards.
    # I took a peek at the Codecademy additional challenge suggestion for this prompt, which
    # has informed my solution:

    carddeck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,\
                         11,11,11,11,12,12,12,12,13,13,13,13]

    card1_pos = random.randint(1,len(carddeck))
    card1 = carddeck.pop(card1_pos)

    card2_pos = random.randint(1,len(carddeck))
    card2 = carddeck.pop(card2_pos)

    print('You picked a {} from the deck.'.format(card1))
    print('The dealer picked a {} from the deck.'.format(card2))

    if card1 > card2:
        print('Your card had the higher number.')
        print('You win!')
        print('You won {} tokens.'.format(betamount))
        newtokens = amount + betamount
    elif card1 < card2:
        print("The dealer's card had the higher number.")
        print('You lose!')
        print('You lost {} tokens.'.format(betamount))
        newtokens = amount - betamount
    else:
        print("It was a tie!")
        print("Your tokens have been returned")
        return amount

    return newtokens
    
# Last, a function that simulates some of the rules of roulette. To be blunt, I don't know much about
# the game, but I do know that you can bet on red or black, or odd or even, or a specific number.
# (Apparently you can also bet on ranges and on high/low but I am not touching these rules.)
# Wikipedia reveals that from 1 to 10 and 19 to 28, odd numbers are red and evens are black.
# from 11 to 18 and 29 to 36, odd numbers are black and evens are red. 0 is green.
# I'mm gonna make my life easier and simulate a single-zero wheel, not a double-zero wheel,
# and I will pretend I didn't see the table on Wikipedia that described the real wagering rules.
# However, I will make things fancy by giving you 5 times your bet if you call the exact right number.

def roulette(number, numberbetamount, oddeven, oddevenbetamount,\
                    redblack, redblackbetamount, amount):

# I need to check that each wager, and the sum of input wagers, obey the checkbalance rules

    checkbalance(amount, numberbetamount)
    if (amount < numberbetamount or numberbetamount < 0):
        return amount
    checkbalance(amount, oddevenbetamount)
    if (amount < oddevenbetamount or oddevenbetamount < 0):
        return amount
    checkbalance(amount, redblackbetamount)
    if (amount < redblackbetamount or redblackbetamount < 0):
        return amount
    totalbet = numberbetamount+oddevenbetamount+redblackbetamount
    checkbalance(amount, totalbet)
    if (amount < totalbet or totalbet < 0):
        return amount

    if (totalbet == 0):
        print("You gotta bet on something! Pick something to wager on.")
        return amount
    
    # first let's see what the roulette wheel actually "rolled"

    ball_landed_on = random.randint(0,36)
    print("The ball landed on {}.".format(ball_landed_on))

    # Now for a heapin' helpin' of nested "if" statements;

    # Asking the player to enter '37' if they do not wish to bet on a particular number is a kludge I readily
    # admit, but it does save me the trouble of having to parse between text input and numeric input.
    if number >= 0 and number <= 36:
        if number == ball_landed_on:
            print('Wow! What a lucky guess! You got the correct number. More winnings for you!')
            print('You won {} tokens.'.format(numberevenbetamount*5))     
            newtokens = amount + (numberbetamount * 5)
            amount = newtokens
        else:
            print('No, the ball did not land on {}.'.format(number))
            print('You lost {} tokens.'.format(numberbetamount))
            newtokens = amount - numberbetamount
            amount = newtokens
    elif number < 0:
        print('Not a valid number guess. Try again.')
        return amount
    elif number > 37:
        print('Not a valid number guess. Try again.')
        return amount
    elif number == 37:
        print('No wager placed on a specific number.')
    
    if oddeven != 'No':
        if oddeven == 'odd' and ball_landed_on%2 == 1:
            print('{} is indeed an odd number!'.format(ball_landed_on))
            print('You win your odd/even bet!')
            print('You won {} tokens.'.format(oddevenbetamount))
            newtokens = amount + oddevenbetamount
            amount = newtokens
        elif oddeven == 'even' and ball_landed_on%2 == 0:
            print('{} is indeed an even number!'.format(ball_landed_on))
            print('You win your odd/even bet!')
            print('You won {} tokens.'.format(oddevenbetamount))
            newtokens = amount + oddevenbetamount
            amount = newtokens
        elif oddeven == 'odd' and ball_landed_on%2 == 0:
            print('{} is not an odd number.'.format(ball_landed_on))
            print('You lose your odd/even bet.')
            print('You lost {} tokens.'.format(oddevenbetamount))
            newtokens = amount - oddevenbetamount
            amount = newtokens
        elif oddeven == 'even' and ball_landed_on%2 == 1:
            print('{} is not an even number!'.format(ball_landed_on))
            print('You lose your odd/even bet.')
            print('You lost {} tokens.'.format(oddevenbetamount))
            newtokens = amount - oddevenbetamount
            amount= newtokens
        else:
            print("Unknown input for 'odd' or 'even' wager. Choices are 'odd', 'even', 'No'. Try again.")
            return amount
    else:
        print("No wager put on odd or even.")

    if redblack != 'No':
        if (redblack != 'red' and redblack != 'black'):
            print("Unknown input for 'red' or 'black' wager. Choices are 'red', 'black', 'No'. Try again.")
            return amount
        # from 1 to 10 and 19 to 28, odd numbers are red and evens are black
        elif (ball_landed_on >= 1 and ball_landed_on <= 10) or (ball_landed_on >= 19 and ball_landed_on <= 28):
            if (ball_landed_on%2 == 1) and (redblack == 'red'):
                print('{} is indeed a red number!'.format(ball_landed_on))
                print('You win your red/black bet!')
                print('You won {} tokens.'.format(redblackbetamount))
                newtokens = amount + redblackbetamount
            elif (ball_landed_on%2 == 0) and (redblack == 'red'):
                print('{} is not a red number. It is black'.format(ball_landed_on))
                print('You lose your red/black bet.')
                print('You lost {} tokens.'.format(redblackbetamount))
                newtokens = amount - redblackbetamount
            elif (ball_landed_on%2 == 1) and (redblack == 'black'):
                print('{} is not a black number. It is red.'.format(ball_landed_on))
                print('You lose your red/black bet.')
                print('You lost {} tokens.'.format(redblackbetamount))
                newtokens = amount - redblackbetamount
            elif (ball_landed_on%2 == 0) and (redblack == 'black'):
                print('{} is indeed a black number!'.format(ball_landed_on))
                print('You win your red/black bet!')
                print('You won {} tokens.'.format(redblackbetamount))
                newtokens = amount + redblackbetamount                                        
        # from 11 to 18 and 29 to 36, odd numbers are black and evens are red
        elif (ball_landed_on >= 11 and ball_landed_on <= 18) or (ball_landed_on >= 29 and ball_landed_on<= 36):
            if (ball_landed_on%2 == 1) and (redblack == 'black'):
                print('{} is indeed a black number!'.format(ball_landed_on))
                print('You win your red/black bet!')
                print('You won {} tokens.'.format(redblackbetamount))
                newtokens = amount + redblackbetamount
            elif (ball_landed_on%2 == 0) and (redblack == 'black'):
                print('{} is not a black number. It is red.'.format(ball_landed_on))
                print('You lose your red/black bet.')
                print('You lost {} tokens.'.format(redblackbetamount))
                newtokens = amount - redblackbetamount
            elif (ball_landed_on%2 == 1) and (redblack == 'red'):
                print('{} is not a red number. It is black.'.format(ball_landed_on))
                print('You lose your red/black bet.')
                print('You lost {} tokens.'.format(redblackbetamount))
                newtokens = amount - redblackbetamount
            elif (ball_landed_on%2 == 0) and (redblack == 'red'):
                print('{} is indeed a red number!'.format(ball_landed_on))
                print('You win your red/black bet!')
                print('You won {} tokens.'.format(redblackbetamount))
                newtokens = amount + redblackbetamount   
        else:
            print('The ball landed on {}, which is green.'.format(ball_landed_on))
            print('You lose your red/black bet.')
            print('You lost {} tokens.'.format(redblackbetamount))
            newtokens = amount - redblackbetamount
    else:
        print("No wager put on red or black.")
        
    return newtokens

#Call your game of chance functions here

def runagame(tokens):
    print("Games of chance are flipacoin, chohan, pickacard, and roulette; type 'halt' to quit.")
    command = input("Game of chance:  ")
    if command == "halt":
        sys.exit()
    elif command == 'flipacoin':
        betamount = input('How much will you bet?   ')
        betamount = int(betamount)
        call = input("Do you call 'heads' or 'tails'?   ")
        tokens = flipacoin(betamount,call,tokens)
        return tokens
    elif command == 'chohan':
        betamount = input('How much will you bet?   ')
        betamount = int(betamount)
        call = input("Do you bet on 'odd' or on 'even'?   ")
        tokens = chohan(betamount,call,tokens)
        return tokens
    elif command == 'pickacard':
        betamount = input('How much will you bet?   ')
        betamount = int(betamount)
        tokens = pickacard(betamount,tokens)
        return tokens
    elif command == 'roulette':
        number = input('Choose a number to bet on, or enter 37 for no bet:   ')
        number = int(number)
        numberbetamount = input("How much will you bet on that number? Enter 0 if you're not betting on a number.   ")
        numberbetamount = int(numberbetamount)
        oddeven = input("Do you bet on 'odd' or on 'even'? If neither, enter No:  ")
        oddevenbetamount = input("How much will you bet on odd or even? Enter 0 if you're not betting on this.   ")
        oddevenbetamount = int(oddevenbetamount)
        redblack = input("Do you bet on 'red or on 'black? If neither, enter No:   ")
        redblackbetamount = input("How much will you bet on red or black? Enter 0 if you're not betting on this.   ")
        redblackbetamount = int(redblackbetamount)
        tokens = roulette(number,numberbetamount,oddeven,oddevenbetamount,\
                                      redblack,redblackbetamount,tokens)
        return tokens
    else:
        print("Unknown game: {}".format(command))
        print("Try again.")
        return tokens 

while True:
    print('You have {} tokens.'.format(tokens))
    tokens = runagame(tokens)

