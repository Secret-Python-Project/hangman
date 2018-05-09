import csv

words = set()  # keeping so that subsequent plays have no repeat words


def play_games():
    load_words_from_file()
    print('Loaded ' + str(len(words)) + ' words')

    # introduce game
    # while user want to play
        # pick a random word
        # present blanks to user
        # test user input


def load_words_from_file():
    with open('10k_words.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            add_if_longer_than_min(row, 4)


def add_if_longer_than_min(row, minimum):
    first_column = row[0]
    if len(first_column) >= minimum:
        words.add(first_column)


if __name__ == '__main__':
    play_games()


# TODO add simple tests
# TODO find better way of interacting with user
