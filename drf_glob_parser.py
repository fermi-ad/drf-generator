#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product
import re
import sys


def main(drf_glob):
    tokens = re.split(r'[{}]', drf_glob)
    iterations = []

    for token in tokens:
        if '..' in token:
            first, second = map(int, token.split('..'))
            iterations.append(list(range(first, second + 1)))
        elif ',' in token:
            iterations.append(token.split(','))
        else:
            if token != '':
                iterations.append([token])

    for result in product(*iterations):
        print(*result, sep='')


if __name__ == '__main__':
    main(sys.argv[1])
