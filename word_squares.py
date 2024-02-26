# Word Squares
# https://techdevguide.withgoogle.com/resources/former-interview-question-word-squares/#!

from collections import defaultdict, deque
from copy import deepcopy


def transform_square(sq):
    return ["".join(s) for s in sq]


# Check to see if sq is a word square between the given indices
def is_symmetric(sq, start, end):  # [[b,a,l,l], [a,r,e,a], [l,e,a,d], [l,a,d,y]]
    for i in range(start, end):
        if not (len(sq[i]) == len(sq)):
            return False
        for j in range(end):
            if not (sq[i][j] == sq[j][i]):
                return False
    return True


# Return the starter square (2D array) for a given word
def get_strtr_sq(word):
    first_row = [*word]
    result = [first_row]
    for c in first_row[1:]:
        row = [c]
        row.extend(['' for _ in range(len(word) - 1)])
        result.append(row)
    return result


# Build a dictionary of letters (keys) to word lists (value)
def build_letter_dict(words):
    res = defaultdict(lambda: [])
    for w in words:
        letter = w[0]
        res[letter].append(w)
    return res


# TODO Optimize for memory
# Building remaining squares from idx and add them to the result list
def add_squares(strtr_sq, letter_dict, result):
    # Short circuit
    if len(strtr_sq) == 1:
        result.append(transform_square(strtr_sq))
        return

    # Initialize
    idx = 1
    q = deque()
    letter = strtr_sq[0][idx]
    for word in letter_dict[letter]:
        sq = deepcopy(strtr_sq)
        sq[idx] = [*word]
        q.append((sq, idx))

    # Find squares
    while q:
        sq, idx = q.popleft()
        if is_symmetric(sq, idx, idx + 1):  # Does adding this word maintain symmetry for this (row, col)?
            if idx + 1 == len(strtr_sq):  # Have we completed the square?
                result.append(transform_square(deepcopy(sq)))
            else:
                words = letter_dict[sq[idx + 1][0]]
                for word in words:
                    new_sq = deepcopy(sq)
                    new_sq[idx + 1] = [*word]
                    q.append((new_sq, idx + 1))


# Given a list of words, return all possible word squares
# Assumptions:
#  * All inputs are 'square shaped' (Number of words == Length of each word)
#  * All inputs are of the same case
#  * Can a word be used more than once? (Yes for now. Fix on next iteration.)
def get_squares(words):
    result = []
    letter_dict = build_letter_dict(words)
    for w in words:
        strtr = get_strtr_sq(w)
        add_squares(strtr, letter_dict, result)
    # return ["".join(s) for s in result]
    return result


if __name__ == '__main__':
    # Assuming all input is at least 'square shaped'
    test1 = [['b', 'a', 'l', 'l'],
             ['a', 'r', 'e', 'a'],
             ['l', 'e', 'a', 'd'],
             ['l', 'a', 'd', 'y']]
    test2 = [['b', 'e', 'l', 'l'],
             ['e', 'r', 'e', 'a'],
             ['l', 'e', 'e', 'd'],
             ['l', 'a', 'd', 'y']]
    test3 = [['a', 'b', 'c', 'd'],
             ['b', 'a', 'e', 'a'],
             ['c', 'e', 'a', 'q'],
             ['d', 'a', 'f', 'z']]
    assert is_symmetric(test1, 0, len(test1))
    assert is_symmetric(test2, 0, len(test2))
    assert is_symmetric(test3, 0, 2)
    assert is_symmetric(test3, 0, 3)
    assert is_symmetric(test3, 1, 3)
    assert not is_symmetric(test3, 2, len(test3))
    assert not is_symmetric(test3, 3, len(test3))

    test3 = 'ball'
    test3_exp = [['b', 'a', 'l', 'l'],
                 ['a', '', '', ''],
                 ['l', '', '', ''],
                 ['l', '', '', '']]
    test3_act = get_strtr_sq('ball')
    for i in range(len(test3)):
        for j in range(len(test3)):
            assert test3_act[i][j] == test3_exp[i][j]

    test4 = ["".join(s) for s in test1]
    print(build_letter_dict(test4))

    print(get_squares(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]))
    print(get_squares(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD", "LEED"]))
    print(get_squares(["THAT", "HASH", "ASIA", "FOOL"]))
