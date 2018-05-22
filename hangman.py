import csv
import time

# configuration parameters, constants as UPPERCASE style wise
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.upper()
SLEEP_TIME = 0.5
STARTING_LIVES = 5
WORD_BANK = '10k_words.txt'

# private instance variables for state
current_lives = STARTING_LIVES
word_length = 0
hidden_word = []
display_word = []


def play_game():
    global current_lives, word_length, hidden_word
    current_lives = STARTING_LIVES

    introduce_game()  # View layer
    word_length = prompt_for_level()
    hidden_word = pick_random_word()
    set_initial_display_word()
    print('Time to start guessing your', len(hidden_word), 'letter word', ''.join(display_word))

    while display_word != hidden_word:
        check_lives()
        print('You have', current_lives, ' left')
        letter = get_player_guess()
        update_display_word(letter)

    print('Waahoooo You Guessed it!')
    does_player_want_to_play_again()


def check_lives():
    if current_lives > 0:
        return
    else:
        game_over()


def does_player_want_to_play_again():
    answer = input('Do you wish to play again? Y/N')

    if answer.upper() == 'Y':
        current_lives
        print()
        print('Staring new game...')
        time.sleep(2 * SLEEP_TIME)
        play_game()
    elif answer.upper() == 'N':
        print()
        print('Goodbye')
        power_down = list('..........')
        while len(power_down) > 0:
            print(''.join(power_down))
            time.sleep(SLEEP_TIME / 2)
            power_down.pop()
        quit()
    else:
        print('Invalid input')
        does_player_want_to_play_again()


def game_over():
    print('You have run out of lives...')
    does_player_want_to_play_again()


def get_player_guess():
    print()
    letter = input('Please guess a letter: ').upper() # get player input, force lowercase for the moment
    if not is_valid_guess(letter):
        print("Opps, that's not right. Please try again.")  # Used " this time because of the ' in sentence
        get_player_guess()
    return letter


def update_display_word(letter):
    if letter in hidden_word:
        print('Found A Letter')
        place_letters(letter)
    else:
        global current_lives

        print('Not in this word, try again...')
        print(''.join(display_word))

        current_lives -= 1


def place_letters(letter):
    for position_in_word in range(len(hidden_word)):
        if hidden_word[position_in_word] == letter:
            display_word[position_in_word] = letter
            print(''.join(display_word))  # TODO if there are multiple letters in loops and displays multiple display_words


def introduce_game():
    print('Welcome to Hangman')
    print('Loading please wait')
    power_up = list('.')
    while len(power_up) < 6:
        print(''.join(power_up))
        time.sleep(SLEEP_TIME / 2)
        power_up.append('.')
    time.sleep(SLEEP_TIME)  # magic number
    print('Before I go get some words...')
    time.sleep(SLEEP_TIME)
    print('What level would you like to play?')
    print()
    time.sleep(SLEEP_TIME)


def prompt_for_level():
    while True:  # keep asking until we get valid input
        print('Enter 1 for Easy')
        print('Enter 2 for Medium')
        print('Enter 3 for Hard')
        level = input('')  # explain why ''

        if level not in ['1', '2', '3']:
            print('Invalid Input')
            print()
        else:
            return get_word_length(level)


def get_word_length(level):
    if level == '1':
        return 5
    elif level == '2':
        return 7
    elif level == '3':
        return 10


#  TODO take hard and medium words away to create easy words
def load_words_from_file():
    words = set()  # Not an instance variable as temporary this function
    with open(WORD_BANK) as file:
        reader = csv.reader(file)
        for row in reader:
            words.add(get_first_column_longer_than(row))
    return words


def get_first_column_longer_than(row):
    first_column = row[0]
    if len(first_column) > word_length:
        return first_column


def pick_random_word():
    words = load_words_from_file()
    word = words.pop()  # Pops word from list
    word = word.upper()  # Forces all UPPER case
    word = list(word)  # Converts the string output into a list for comparison.
    return word

def set_initial_display_word():
    for hidden_letter in hidden_word:
        if hidden_letter in ALPHABET:
            display_word.append('.')  # put "." for every letter in hidden word
        else:
            display_word.append('?')  # leave as check during development


def is_valid_guess(letter_guessed):
    if len(letter_guessed) != 1:  # single characters only
        return False
    elif letter_guessed not in ALPHABET:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest

    # doctest.testmod()  # for in-line tests
    # doctest.testfile("hangman_examples.md")
    play_game()
