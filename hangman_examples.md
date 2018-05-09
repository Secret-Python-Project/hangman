The ``Hangman`` module
======================

Using ``Hangman``
-------------------

This is an example text file in reStructuredText format.

    >>> from hangman import get_first_column_longer_than

    >>> get_first_column_longer_than(['testCol1', 'testCol2'], 4)
    'testCol1'

    >>> get_first_column_longer_than(['testCol1', 'testCol2'], 8)
