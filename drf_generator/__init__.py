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
        if len(first) > 1:
            pad_length = len(first)
            pad_character = first[0]

            return list(map(
                lambda x: f'{x:{pad_character}{pad_length}d}',
                range(int(first), int(second) + 1)
            ))
        else: # In case we don't have a padded number
            return list(range(int(first), int(second) + 1))
    else:
        return list(char_range(first, second))


def generate(drf_glob, debug=False):
    tokens = re.split(r'[{}]', drf_glob)
    iterations = []
    results = []

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
        results.append(''.join(map(str, result)))

    return results


if __name__ == '__main__':
    generate(sys.argv[1])
