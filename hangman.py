import csv
import time

# configuration parameters, constants as UPPERCASE style wise
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.upper()
SLEEP_TIME = 0.5
STARTING_LIVES = 5
WORD_BANK = '10k_words.txt'

# private instance variables for state
lives = STARTING_LIVES
hidden_word = []
display_word = []


def play_games():
    wants_to_play = True

    while wants_to_play:
        play_single_game()
        wants_to_play = prompt_to_play_again()


def play_single_game():
    global lives, hidden_word
    lives = STARTING_LIVES

    introduce_game()  # View layer
    word_length = prompt_for_level()
    hidden_word = pick_random_word(word_length)
    set_initial_display_word()
    print('Time to start guessing your', len(hidden_word), 'letter word', ''.join(display_word))

    while display_word != hidden_word:
        if lives == 0:
            print('You have run out of lives...')
            return  # note leave the game (see break, return, continue differences)
        print('You have', lives, 'left')  # note , adds spaces for you
        letter = get_player_guess()
        update_display_word(letter)

    print('Waahoooo You Guessed it!')


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


def pick_random_word(length):
    words = load_words_from_file(length)
    word = words.pop()  # Pops word from list
    word = word.upper()  # Forces all string output into a list for comparison.
    return word


def set_initial_display_word():
    for hidden_letter in hidden_word:
        if hidden_letter in ALPHABET:
            display_word.append('.')  # put "." for every letter in hidden word
        else:
            display_word.append('?')  # leave as check during development


def get_player_guess():
    while True:  # keep trying for valid input
        print()
        letter = input('Please guess a letter: ').upper() # get player input, force lowercase for the moment
        if not is_valid_guess(letter):
            print("Opps, that's not right. Please try again.")  # Used " this time because of the ' in sentence
        else:
            return letter


def is_valid_guess(letter_guessed):
    if len(letter_guessed) != 1:  # single characters only
        return False
    elif letter_guessed not in ALPHABET:
        return False
    else:
        return True


def update_display_word(letter):
    if letter in hidden_word:
        print('Found A Letter')
        place_letters(letter)
    else:
        global lives

        print('Not in this word, try again...')
        print(''.join(display_word))

        lives -= 1


def prompt_to_play_again():
    while True:  # keep on asking!
        answer = input('Do you wish to play again? Y/N')

        if answer.upper() == 'Y':
            print()
            print('Starting new game...')
            time.sleep(2 * SLEEP_TIME)
            return True
        elif answer.upper() == 'N':
            print()
            print('Goodbye')
            power_down = list('..........')
            while len(power_down) > 0:
                print(''.join(power_down))
                time.sleep(SLEEP_TIME / 2)
                power_down.pop()
            return False
        else:
            print('Invalid input')


def place_letters(letter):
    for position_in_word in range(len(hidden_word)):
        if hidden_word[position_in_word] == letter:
            display_word[position_in_word] = letter
            print(''.join(display_word))  # TODO if there are multiple letters in loops and displays multiple display_words


def get_word_length(level):
    if level == '1':
        return 5
    elif level == '2':
        return 7
    elif level == '3':
        return 10


#  TODO take hard and medium words away to create easy words
def load_words_from_file(length):
    words = set()  # Not an instance variable as temporary this function
    with open(WORD_BANK) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row[0]) == length:
                words.add(row[0])
    return words


if __name__ == '__main__':
    play_games()
