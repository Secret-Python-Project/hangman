import csv
import time

# configuration parameters
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
sleep_time = 0.5  # TODO constants as UPPERCASE style wise?

# private instance variables for state
starting_lives = 5
current_lives = starting_lives
difficulty = 0  # TODO consider enum
hidden_word = []
display_word = []


def play_game():


    introduce_game() # View layer
    pick_difficulty()  # TODO separate View and Controller
    set_random_hidden_word()  # could be load_words_from_file().pop()
    set_initial_display_word()
    print('Time to start guessing your', len(hidden_word), 'letter word' , ''.join(display_word))
    print("Hidden word: ", ''.join(hidden_word))  # TODO remove:
    print(type(hidden_word))

    while display_word != hidden_word:
        check_lives()
        print('You have',current_lives,' left')
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
        print('staring new game...')
        time.sleep(2 * sleep_time)
        play_game()

    elif answer.upper() == 'N':
        print()
        print('Goodbye')
        power_down = list('..........')
        while len(power_down) > 0:
            print(''.join(power_down))
            time.sleep(sleep_time / 2)
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

        print('Not in this word, try again...') # TODOif in correct it takes two goes to get the right letter in place
        current_lives -= 1


def place_letters(letter):
    for position_in_word in range(len(hidden_word)):
        if hidden_word[position_in_word] == letter:
            display_word[position_in_word] = letter
            print(display_word)  # TODO if there are multiple letters in loops and displays multiple display_words


def introduce_game():
    print('Welcome to Hangman')
    print('Loading please wait')
    power_up = list('.')
    while len(power_up) < 6:
        print(''.join(power_up))
        time.sleep(sleep_time / 2)
        power_up.append('.')
    time.sleep(sleep_time)  # magic number
    print('Before I go get some words...')
    time.sleep(sleep_time)
    print('What Difficulty would you like to play?')
    print()
    time.sleep(sleep_time)


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
    global difficulty

    if level == '1':
        difficulty = 5  # TODO how to formally reference the global? ALSO needs Enum-ing
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
    hidden_word = words.pop() # Pops word from list
    hidden_word = hidden_word.upper() # Forces all UPPER case
    hidden_word = list(hidden_word) # Converts the string output into a list for comparison.

    # TODO make hidden_word upper case


def set_initial_display_word():
    for hidden_letter in hidden_word:
        if hidden_letter in alphabet:
            display_word.append('.')  # put "." for every letter in hidden word
        else:
            display_word.append('?')  # leave as check during development


def is_valid_guess(letter_guessed):
    if len(letter_guessed) != 1:  # single characters only
        return False
    elif letter_guessed not in alphabet:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest

    # doctest.testmod()  # for in-line tests
    # doctest.testfile("hangman_examples.md")
    play_game()
