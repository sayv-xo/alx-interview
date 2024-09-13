#!/usr/bin/python3
"""
Checks for a valid move in a chess board
"""
import sys


def main(argv):
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    number = int(argv[1])

    if number < 4:
        print("N must be at least 4")
        exit(1)

    def queens(number, i=0, a=[], b=[], c=[]):
        """Evaluating possible positions"""
        if i < number:
            for j in range(number):
                if j not in a and i + j not in b and i - j not in c:
                    yield from queens(number, i + 1, a + [j], b + [i + j],
                                      c + [i - j])
        else:
            yield a

    solutions = list(queens(number))
    for solution in solutions:
        print([[i, solution[i]] for i in range(number)])


if __name__ == "__main__":
    main(sys.argv)