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
            words.add(get_first_column_longer_than(row, 3))


def get_first_column_longer_than(row, minimum):
    """Adds words longer than supplied min length

    >>> get_first_column_longer_than(['testCol1', 'testCol2'], 4)
    'testCol1'

    >>> get_first_column_longer_than(['testCol1', 'testCol2'], 8)

    """
    first_column = row[0]
    if len(first_column) > minimum:
        return first_column


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    play_games()


# TODO add simple tests
# TODO find better way of interacting with user
