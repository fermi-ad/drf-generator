#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product
import re
import sys


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def token_range(first, second):
    if first.isnumeric():
        pad_length = len(first)
        pad_character = first[0]

        return list(map(
            lambda x: f'{x:{pad_character}{pad_length}d}',
            range(int(first), int(second) + 1)
        ))
    else:
        return list(char_range(first, second))


def main(drf_glob, debug=False):
    tokens = re.split(r'[{}]', drf_glob)
    iterations = []

    if debug:
        print(tokens)

    for token in tokens:
        if '..' in token:
            first, second = token.split('..')
            iterations.append(token_range(first, second))
        elif ',' in token:
            iterations.append(token.split(','))
        else:
            if token != '':
                iterations.append([token])

    for result in product(*iterations):
        print(*result, sep='')


if __name__ == '__main__':
    main(sys.argv[1])
