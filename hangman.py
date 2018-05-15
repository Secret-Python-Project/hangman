import csv
import time

# configuration parameters
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # TODO put this somewhere better
sleep_time = 0.5  # TODO constants as UPPERCASE style wise?

# private instance variables for state
lives_left = 10
difficulty = 0  # TODO consider enum
hidden_word = ''
display_word = ''


def play_game():
    # TODO are these caches?
    valid_input = False
    game_over = False

    introduce_game() # View layer
    pick_difficulty()  # TODO separate View and Controller
    set_random_hidden_word()  # could be load_words_from_file().pop()
    print("Hidden word:", hidden_word)
    set_initial_display_word()
    print(display_word)

    while not game_over:
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
                print(display_word)
                if '_ ' not in display_word:
                    print('Waahoooo You Guess it!')
                    game_over = True
            else:
                for letters in range(len(hidden_word)):
                    if letter_guessed not in hidden_word:
                        lives_left - 1
                        print('Opps, thats not right')
                        print('You have ', lives_left, 'lives left')
                    elif letter_guessed in hidden_word:
                        print(letter_guessed)


def introduce_game():
    print('Welcome to Hangman')
    time.sleep(sleep_time)  # magic number
    print('Before I go get some words...')
    time.sleep(sleep_time)
    print('What Difficulty would you like to play?')
    time.sleep(sleep_time)
    print()


def pick_difficulty():
    print('Enter 1 for Easy')
    print('Enter 2 for Medium')
    print('Enter 3 for Hard')
    level = input('')  # explain why ''

    if level not in ['1', '2', '3']:
        print('Invalid Input')
        print()
        pick_difficulty()
    else:
        assign_difficulty(level)


def assign_difficulty(level):
    if level == '1':
        difficulty = 5  # TODO how to formally reference the global?

    elif level == '2':
        difficulty = 7

    elif level == '3':
        difficulty = 10


#  TODO take hard and medium words away to create easy words
def load_words_from_file():
    words = set()  # Not an instance variable as temporary this function
    with open('10k_words.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            words.add(get_first_column_longer_than(row))
    return words


def get_first_column_longer_than(row):
    first_column = row[0]
    if len(first_column) > difficulty:
        return first_column


def set_random_hidden_word():
    words = load_words_from_file()
    hidden_word = words.pop()
# TODO make hidden_word upper case
    '''
    For every letter in hidden_word make it upper case
    '''


def set_initial_display_word():
    for hidden_letter in hidden_word:
        if hidden_letter in alphabet:
            display_word.append('.')  # put "_ " for every letter in hidden word
        else:
            display_word.append('?')  # leave as check during development


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
