import csv
import time

# configuration parameters
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # TODO put this somewhere better
sleep_time = 0.5  # TODO constants as UPPERCASE style wise?

# private instance variables for state
# TODO add lives
difficulty = 0  # TODO consider enum
hidden_word = []
display_word = []


def play_game():
    introduce_game() # View layer
    pick_difficulty()  # TODO separate View and Controller
    set_random_hidden_word()  # could be load_words_from_file().pop()
    set_initial_display_word()

    print("Hidden word: ", hidden_word)  # TODO remov
    print(type(hidden_word))
    print(display_word)
    print(type(display_word))

    while str(display_word) != hidden_word:
        letter = get_player_guess()
        update_display_word(letter)
        print(display_word)

    print('Waahoooo You Guessed it!')


def get_player_guess():
    letter = input('\nPlease guess a letter: \n').lower() # get player input, force lowercase foe the moment
    if not is_valid_guess(letter):
        print("Opps, that's not right. Please try again.")  # Used " this time because of the ' in sentence
        get_player_guess()
    return letter


def update_display_word(letter):
    if letter in hidden_word:
        print('Found A Letter')
        

    else:
        print('Not in this word, try again...')
        # Lose a life
        # Tell Player how many lives left
    # TODO write in test-driven way

# def process_letter(letter):
#     if letter in hidden_word:
#         for index in hidden_word:
#             if hidden_word[index] == letter:
#                 display_word[index] = letter
#         print(display_word)
#     else:
#         for letters in range(len(hidden_word)):
#             if letter not in hidden_word:
#                 print('Opps, thats not right')
#             elif letter in hidden_word:
#                 print(letter)


def introduce_game():
    print('Welcome to Hangman')
    time.sleep(sleep_time)  # magic number
    print('Before I go get some words...')
    time.sleep(sleep_time)
    print('What Difficulty would you like to play?\n')
    time.sleep(sleep_time)


def pick_difficulty():
    print('Enter 1 for Easy')
    print('Enter 2 for Medium')
    print('Enter 3 for Hard')
    level = input('')  # explain why ''

    if level not in ['1', '2', '3']:
        print('Invalid Input\n')
        pick_difficulty()
    else:
        assign_difficulty(level)


def assign_difficulty(level):
    global difficulty

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
    global hidden_word
    hidden_word = list(words.pop()) # Convertys the string output into a list for comparison.


    # TODO make hidden_word upper case


def set_initial_display_word():
    for hidden_letter in hidden_word:
        if hidden_letter in alphabet:
            display_word.append('.')  # put "_ " for every letter in hidden word
        else:
            display_word.append('?')  # leave as check during development


def is_valid_guess(letter_guessed):
    if len(letter_guessed) != 1:  # single characters only
        return False
    elif letter_guessed not in alphabet:
        return False
    else:
        return True


def user_wants_to_play(): # TODO make this richerer
    return True

if __name__ == '__main__':
    import doctest

    # doctest.testmod()  # for in-line tests
    # doctest.testfile("hangman_examples.md")
    play_game()
