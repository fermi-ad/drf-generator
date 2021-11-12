#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for drf_generator package."""

from pathlib import Path

import pytest

import drf_generator.generator as drf_generator

parent_path = Path(__file__).parent
first_validation_file = parent_path.joinpath('test_validate1.txt').resolve()
second_validation_file = parent_path.joinpath(
    'test_validate2.txt').resolve()


def equal(first, second):
    """
    Check the equivalence of two objects.

    :param first: First object to compare.
    :param second: Second object to compare.
    :return: True if the objects are equal, False otherwise.
    """
    return first == second


@pytest.mark.parametrize('first,second,expected,comparator', [
    ('A', 'F', ['A', 'B', 'C', 'D', 'E', 'F'], equal),
    ('F', 'A', [], equal),
    ('1', '6', ['1', '2', '3', '4', '5', '6'], equal),
    ('6', '1', [], equal),
])
def test_char_range(first, second, expected, comparator):
    """
    Test the char_range function.

    :param first: First character.
    :param second: Second character.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.char_range(first, second))
    assert comparator(result, expected)


@pytest.mark.parametrize('first,second,expected,comparator', [
    ('A', 'F', ['A', 'B', 'C', 'D', 'E', 'F'], equal),
    ('F', 'A', [], equal),
    ('1', '6', [1, 2, 3, 4, 5, 6], equal),
    ('6', '1', [], equal),
    ('001', '006', ['001', '002', '003', '004', '005', '006'], equal),
    ('006', '001', [], equal),
    ('008', '012', ['008', '009', '010', '011', '012'], equal),
    ('000998', '001002', ['000998', '000999',
     '001000', '001001', '001002'], equal),
])
def test_token_range(first, second, expected, comparator):
    """
    Test the token_range function.

    :param first: First token.
    :param second: Second token.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.token_range(first, second))
    assert comparator(result, expected)


@pytest.mark.parametrize('tests,expected,comparator', [
    (['{I,R}:VT001'], ['I:VT001', 'R:VT001'], equal),
    (['{A,B,C,D}:VT001'], ['A:VT001', 'B:VT001', 'C:VT001', 'D:VT001'], equal),
    (['I{}:VT001'], ['I:VT001'], equal),
    (['I:VT{001..002}'], ['I:VT001', 'I:VT002'], equal),
    (['I:VT{005..015}'], ['I:VT005', 'I:VT006', 'I:VT007', 'I:VT008', 'I:VT009',
                          'I:VT010', 'I:VT011', 'I:VT012', 'I:VT013', 'I:VT014',
                          'I:VT015'], equal),
    (['I:VT{003..001}'], [], equal),
    (['{I,R}:VT{001..003}'], ['I:VT001', 'I:VT002', 'I:VT003', 'R:VT001',
                              'R:VT002', 'R:VT003'], equal),
    (['{I,R}:VT001', 'I:VT{001..002}'], [
     'I:VT001', 'R:VT001', 'I:VT001', 'I:VT002'], equal),
    (['AB}C{D'], ['ABCD'], equal),
    (['001..002'], ['001', '002'], equal),
    (['A}BC,DE'], ['ABC', 'ADE'], equal),
])
def test_generate(tests, expected, comparator):
    """
    Test the generate function.

    :param tests: Tests to run.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.generate(*tests))
    assert comparator(result, expected)


@pytest.mark.parametrize('validatee,validator,expected,comparator', [
    (first_validation_file, 'I:VT{005..015}', [], equal),
    (second_validation_file, 'I:VT{005..015}',
     ['ABCDEF', '1234', 'xYz'], equal),
])
def test_verify(validatee, validator, expected, comparator):
    """
    Test the verify function.

    :param validatee: File to validate.
    :param validator: Validator.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.verify(validatee, validator))
    assert comparator(result, expected)
