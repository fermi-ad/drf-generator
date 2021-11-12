#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from itertools import product


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
        else:  # In case we don't have a padded number
            return list(range(int(first), int(second) + 1))
    else:
        return list(char_range(first, second))


def generate(*drf_globs, debug=False):
    results = []

    def parse_globs(drf_globs):
        for drf_glob in drf_globs:
            # Parse nested lists and tuples
            if type(drf_glob) in [list, tuple]:
                parse_globs(drf_glob)
                break

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
                results.append(''.join(map(str, result)))

    parse_globs(drf_globs)

    return results


def verify(test_file, *globs):
    test_requests = generate(globs)
    valid_results = []

    with open(test_file) as file:
        for line in file.readlines():
            valid_results.append(line.strip())

    no_matches = []

    for request in valid_results:
        if request not in test_requests:
            no_matches.append(request)

    return True if len(no_matches) == 0 else no_matches
