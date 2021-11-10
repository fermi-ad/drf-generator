#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Expose CLI interface."""

import sys

from drf_generator.generator import generate

if __name__ == '__main__':
    print(generate(sys.argv[1:]))
