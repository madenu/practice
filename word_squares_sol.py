#!/usr/bin/env python
import collections
import sys


def find_word_squares(words):
    # Preprocess words: O(#words * word-length) time and space
    words_by_letter_position = collections.defaultdict(set)
    for word in words:
        for index, letter in enumerate(word):
            words_by_letter_position[(index, letter)].add(word)

    # For each word, see if we can make a square.  O(#words * word-length^2/2)
    # for speed, assuming that set intersection is ~O(1) for small sets.
    # Worst-case storage is O(#words * word-length) for very very contrived
    # 'words'.  Normal English words will result in much smaller storage demand;
    # there is a practical maximum of ~170,000 English words.
    for word in words:
        # Initialize a set of incomplete possible squares; each item is an N-tuple
        # of words that are valid but incomplete word squares.  We could also do
        # depth-first via recursion/generators, but this approach is a little
        # simpler to read top-to-bottom.
        possible_squares = {(word,)}

        # As long as we have any incomplete squares:
        while possible_squares:
            sq = possible_squares.pop()
            # When matching an incomplete square with N words already present,
            # we need to match any prospective words to the tuples formed by
            # (N, Nth character in word 0), (N, Nth character in word 1), ...
            # Only words which satisfy all of those restrictions can be added.
            keys = [(i, sq[i][len(sq)]) for i in range(len(sq))]  # TODO Check lenght of word so as not to get an index out of bound error.
            possible_matches = [words_by_letter_position[key] for key in keys]
            for valid_word in set.intersection(*possible_matches):
                valid_square = sq + (valid_word,)
                # Save valid square in 'ret' if it's complete, or save it as
                # a work-to-do item if it's not.
                if len(valid_square) == len(word):
                    yield valid_square
                else:
                    possible_squares.add(valid_square)


if __name__ == '__main__':
    for square in find_word_squares(sys.argv[1:]):
        print('\n'.join(square))
        print()