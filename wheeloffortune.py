# single player wheel of fortune played in the terminal window

import random

WHEEL = (50, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 250, 250 ,250, 500, 500, 750, 750, 1000, 2000, 5000, 10000, "Bankrupt", "Bankrupt")
VOWEL_COST = 250
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
VOWELS = 'AEIOU'

#spinTheWheel takes inputs of the string holding the solution to the puzzle
#and an integer representing the player's current balance
#It generates random stakes by simulating the spin of a wheel,
#gives the player a chance to guess a consonant in the puzzle solution,
#and awards money or takes it away depending on the accuracy of the guess
#It returns an integer representing the player's current balance,
#a string holding the consonant they guessed,
#and a boolean value indicating if their guess was correct
def spinTheWheel(puzzle_solution,current_balance):
    print('Slower and slower, the wheel spins. Then finally, it comes to a stop on...')
    index = random.randint(0,23) #simulation of spinning the wheel
    if index == 22 or index == 23:
        current_balance = 0
        print('BANKRUPT!')
        return current_balance, '' #no boolean value as no guess was made
    spin = WHEEL[index]
    print('$' + str(spin) + '!')
    print()
    consonant = input('The crowd holds its breath. What consonant will you guess? ').upper()
    print()
    while consonant not in CONSONANTS: #loop to fix intitial incorrect user input
        print('To my knowledge,',consonant,'is not a consonant.')
        consonant = input('Care to try again? ').upper()
        print()
    if consonant in puzzle_solution: #correct guess
        occurances = puzzle_solution.count(consonant)
        current_balance += (spin * occurances)
        print('The silence is broken by thunderous applause!')
        print(consonant,'appears in the mystery phrase', occurances,'times!')
        print('You have won $' + str(spin * occurances) + '!')
        return current_balance, consonant, True
    else: #incorrect guess
        current_balance += (-1 * spin)
        print('The silence subsides into a symphony of sighs and whispers.')
        print(consonant,'is nowhere to be found in the mystery phrase,')
        print('and your pot of gold is now $' + str(spin), 'lighter.')
        return current_balance, consonant, False

#buyAVowel takes inputs of the string holding the solution to the puzzle
#and an integer representing the player's current balance
#It checks to make sure the player has adiquate funds, and subtracts $250 if it's there to take,
#and gives the player a chance to guess a vowel in the puzzle solution
#It returns an integer representing the player's current balance,
#a string holding the vowel they guessed,
#and a boolean value indicating if their guess was correct
def buyAVowel(puzzle_solution,current_balance):
    print("That'll cost you $250.")
    print()
    if current_balance < VOWEL_COST: #checking player balance for the $250 needed
        print("What?! You're saying you don't have the cash on you?")
        print('Well, come back when you do.')
        return current_balance, '' #no boolean value as no guess was made
    print("Transaction complete. Now, let's not keep the crowd waiting any longer.")
    print()
    vowel = input("The time has come to choose your vowel. ").upper()
    print()
    while vowel not in VOWELS: #loop to fix inital incorrect user input
        print("I'm afraid only vowels are up for sale.",vowel,"is not a vowel.")
        vowel = input("Care to try again? ").upper()
        print()
    if vowel in puzzle_solution: #correct guess
        current_balance += -VOWEL_COST
        occurances = puzzle_solution.count(vowel)
        print("The crowd goes wild!")
        print(vowel,'appears in the mystery phrase', occurances,'times!')
        return current_balance, vowel, True
    else: #incorrect guess
        current_balance += -VOWEL_COST
        print('A cricket cheers. The rest of the room is silent.')
        print(vowel,'is nowhere to be found in the mystery phrase.')
        return current_balance, vowel, False

#solveThePuzzle takes inputs of the string holding the solution to the puzzle
#and an integer representing the player's current balance
#It gives the player a chance to guess the solution to the puzzle,
#compares the guess with the actual solution,
#and congratulates the player or resets their current balance to zero
#It returns an integer representing the player's current balance
#and a boolean value indicating if their guess was correct
def solveThePuzzle(puzzle_solution,current_balance):
    print("The time has come to claim your fame!")
    print("Guess correctly and you'll win the game!")
    print("But if you're wrong, your golden hoard will go up in flame.")
    print()
    print("Be sure to use single spaces!")
    print()
    guess = input("So, what is the mystery phrase? ").upper()
    print()
    if guess == puzzle_solution: #correct guess
        print('The crowd leaps to their feet to give a standing ovation well deserved.')
        print('Brilliantly done! You are indeed correct!')
        return current_balance, True
    else: #incorrect guess
        print('Poof! Like the morning mist chased away by the summer sun, your hard earned cash disappears.')
        print('But wait, is that the glimmer of more gold I see on the horizon?!')
        print('This guess may not have been the answer, but we may yet see this quest fullfilled!')
        if current_balance > 0:
            current_balance = 0
        return current_balance, False

#phrasePrint takes inputs of the string holding the solution to the puzzle
#a string holding the vowels guessed,
#and a string holding the consonants guessed
#It replaces all characters of the solution not yet guessed with underscores
#and returns a string containing the solution with the unknown letters shown as underscores
def phrasePrint(puzzle_solution,vowels_guessed,consonants_guessed):
    guesses = ' ' + vowels_guessed + consonants_guessed
    underscores_and_letters = ''
    for letter in puzzle_solution:
        if letter in guesses:
            underscores_and_letters += letter + ' ' #keep guessed letters and spaces
        else:
            underscores_and_letters += '_ ' #replace unknown letters with underscores
    underscores_and_letters = underscores_and_letters[:-1] #to remove extra space at the end
    return underscores_and_letters

def main():
    current_balance = 0
    vowels_guessed = ''
    consonants_guessed = ''
    looping = True
    turn_options = ('spin','vowel','solve')
    PhraseBank = open('phrasebank.txt').read().splitlines()
    Phrase_i = random.randint(0,99)
    puzzle_solution = PhraseBank[Phrase_i]
    if Phrase_i < 20: #phrase category determined by index (aka location in PhraseBank)
        puzzle_category = 'Before and After'
    elif Phrase_i < 40:
        puzzle_category = 'Song Lyrics'
    elif Phrase_i < 60:
        puzzle_category = 'Around the House'
    elif Phrase_i < 80:
        puzzle_category = 'Food and Drink'
    else:
        puzzle_category = 'Same Name'
    print('Welcome to the Wheel of Fortune!')
    print()
    print('Your mystery phrase is:')
    print(phrasePrint(puzzle_solution,vowels_guessed,consonants_guessed))
    print()
    print('We chose it from the category:', puzzle_category)
    print()
    print('Currently, your pot of gold contains: $' + str(current_balance))
    print()
    while looping: #loop for player turns
        print('You stand at a crossroads with three choices before you.')
        print('Would you like test your luck and give our Wheel a Spin? (type "spin") ')
        print('Perhaps you would prefer to attend our vowel auction? (type "vowel") ')
        turn = input('Or are you ready to unveil the mystery phrase and solve our puzzle? (type "solve") ').lower()
        print()
        while turn not in turn_options: #loop to fix initial incorrect user input
            print("This crossroads only has three paths to choose from, and that's not one of them.")
            turn = input('Care to try again? ').lower()
            print()
        if turn == 'spin':
            spin_results = list(spinTheWheel(puzzle_solution,current_balance))
            current_balance = spin_results[0]
            consonants_guessed += spin_results[1]
        elif turn == 'vowel':
            vowel_results = list(buyAVowel(puzzle_solution,current_balance))
            current_balance = vowel_results[0]
            vowels_guessed += vowel_results[1]
        elif turn == 'solve':
            solve_results = list(solveThePuzzle(puzzle_solution,current_balance))
            current_balance = solve_results[0]
            if solve_results[1] == True:
                looping = False
        print()
        if looping != False:
            print('Your mystery phrase is:')
            print(phrasePrint(puzzle_solution,vowels_guessed,consonants_guessed))
            print()
            print('We chose it from the category:', puzzle_category)
            print()
            print('Vowels Guessed:',vowels_guessed)
            print('Consonants Guessed:',consonants_guessed)
        else:
            print('Congratulations! Victory is yours!')
        if len(consonants_guessed) == 21 and len(vowels_guessed) == 5: #game over, player loses
            looping = False
            current_balance = 0
            print()
            print('Sometimes, the puzzle is just TOO mysterious.')
            print("It looks like you've guessed all the letters,")
            print("but still haven't guessed the answer to the greater mystery.")
            print()
            print("I'm afraid that means the puzzle is the only winner here.")
            print('Better luck next time!')
            print()
            print('Your pot of gold is empty.')
            print('Final winings: $' + str(current_balance))
        elif looping == False:
            if current_balance >= 0:
                print('Your pot of gold contains: $' + str(current_balance))
            else:
                current_balance = 0
                print('Your pot of gold contains: $' + str(current_balance))
        else:
            print('Your current pot of gold contains: $' + str(current_balance))
            print()

if __name__ == '__main__':
    main()
