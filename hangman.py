import csv
import time

words = set()  # keeping so that subsequent plays have no repeat words

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # TODO put this somewhere better
lives_left = 10
game_over = False


def play_game():
    row = '0'
    valid_input = False
    introduce_game() # Input Layer
    difficulty = set_game_start_conditions()
    hidden_word = pick_random_word_from_set(difficulty) # pick a random word (psudeo atm)
    display_word = make_blank_spaces(hidden_word)
    show_blank_spaces(display_word) # present blanks to user

    while not valid_input:
        letter_guessed = get_player_guess()
        valid_input = validate_guess(letter_guessed)
        if valid_input == False:
            print("Opps, that's not right. Please try again.")  # Used " this time because of the ' in sentence
        else:
            valid_input = True
        if letter_guessed in hidden_word:
            for i in range(len(hidden_word)):
                if hidden_word[i] == letter_guessed:
                    display_word[i] = letter_guessed
            show_blank_spaces(display_word)
            if '_ ' not in display_word:
                print('Waahoooo You Guess it!')
        else:
            evaluate_guess(letter_guessed,hidden_word)

            hidden_word(display_word)


def set_game_start_conditions():
    level = pick_level()  # input Layer
    check_level_validity(level)  # Game Logic
    difficulty = assign_difficulty(level)  # Game Logic
    load_words_from_file(difficulty)
    print('Loaded ' + str(len(words)) + ' words')

    return difficulty


def introduce_game():
    print('Welcome to Hangman')
    time.sleep(.5)
    print('Before I go get some words...')
    time.sleep(.5)
    print('What Difficulty would you like to play?')
    time.sleep(.5)
    print()

def pick_level():
    print('Enter 1 for Easy')
    print('Enter 2 for Medium')
    print('Enter 3 for Hard')
    level = input('')
    return level


def check_level_validity(level):
    if level not in ['1', '2', '3']:
        print('Invalid Input')
        print()
        set_game_start_conditions()


def assign_difficulty(level):
    difficulty = 0

    if level == '1':
        difficulty = 5

    elif level == '2':
        difficulty = 7

    elif level == '3':
        difficulty = 10
    print(difficulty)
    return difficulty

#  TODO take hard and medium words away to create easy words
def load_words_from_file(difficulty):
    with open('10k_words.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            words.add(get_first_column_longer_than(row, difficulty))


def get_first_column_longer_than(row, difficulty):
    first_column = row[0]
    if len(first_column) > difficulty:
        print(first_column)
        return first_column


def pick_random_word_from_set(difficulty):
    hidden_word = words.pop()
    print()
    print(hidden_word)  # check to see what hidden word is
    print()
    return hidden_word
# TODO make hidden_word upper case
    '''
    For every letter in hidden_word make it upper case
    '''


def make_blank_spaces(hidden_word):
    print('The word is', len(hidden_word), 'characters long')
    display_word = []  # create an empty list what the word can be revealed in
    for hidden_letters in range(len(hidden_word)):
        if hidden_word[hidden_letters] in alphabet:
            display_word.append('_ ')  # put "_ " for every letter in hidden word
        else:
            display_word.append(hidden_word[hidden_letters])
    print('Displayword:', display_word)
    return display_word


def show_blank_spaces(display_word):
    word = ''
    for letters in range(len(display_word)):
        word += display_word[letters]  # increment through word
    print('WORD', word)


def get_player_guess():
    print()
    letter_guessed = input('Please guess a letter: ').lower() # get player input, force lowercase foe the moment
    print()
    return letter_guessed

def validate_guess(letter_guessed):
    if len(letter_guessed) > 1 or letter_guessed not in alphabet:
        valid_input = False
    else:
        return True


def evaluate_guess(letter_guessed, hidden_word): # TODO Validate input is a single character only and not numbers or specials
    for letters in range(len(hidden_word)):
        if letter_guessed not in hidden_word:
            lives_left - 1
            print ('Opps, thats not right')
            print('You have ', lives_left, 'lives left')
        elif letter_guessed in hidden_word:
            print(letter_guessed)

'''
def game_over(display_word):
    if lives_left < 0:
        print('Game Over Man, Game Over')
    elif '_ ' not in display_word:
        print('Awesome, You have won!')
'''

def user_wants_to_play(): # TODO make this richerer
    return True

if __name__ == '__main__':
    import doctest

    # doctest.testmod()  # for in-line tests
    # doctest.testfile("hangman_examples.md")
    play_game()


# TODO add simple tests
