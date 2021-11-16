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


@pytest.mark.parametrize('first,second,expected', [
    ('A', 'F', ['A', 'B', 'C', 'D', 'E', 'F']),
    ('F', 'A', []),
    ('1', '6', ['1', '2', '3', '4', '5', '6']),
    ('6', '1', []),
])
def test_char_range(first, second, expected):
    """
    Test the char_range function.

    :param first: First character.
    :param second: Second character.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.char_range(first, second))
    assert result == expected


@pytest.mark.parametrize('first,second,expected', [
    ('A', 'F', ['A', 'B', 'C', 'D', 'E', 'F']),
    ('F', 'A', []),
    ('1', '6', [1, 2, 3, 4, 5, 6]),
    ('6', '1', []),
    ('001', '006', ['001', '002', '003', '004', '005', '006']),
    ('006', '001', []),
    ('008', '012', ['008', '009', '010', '011', '012']),
    ('000998', '001002', ['000998', '000999',
     '001000', '001001', '001002']),
])
def test_token_range(first, second, expected):
    """
    Test the token_range function.

    :param first: First token.
    :param second: Second token.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.token_range(first, second))
    assert result == expected


@pytest.mark.parametrize('tests,expected', [
    (['{I,R}:VT001'], ['I:VT001', 'R:VT001']),
    (['{A,B,C,D}:VT001'], ['A:VT001', 'B:VT001', 'C:VT001', 'D:VT001']),
    (['I{}:VT001'], ['I:VT001']),
    (['I:VT{001..002}'], ['I:VT001', 'I:VT002']),
    (['I:VT{005..015}'], ['I:VT005', 'I:VT006', 'I:VT007', 'I:VT008', 'I:VT009',
                          'I:VT010', 'I:VT011', 'I:VT012', 'I:VT013', 'I:VT014',
                          'I:VT015']),
    (['I:VT{003..001}'], []),
    (['{I,R}:VT{001..003}'], ['I:VT001', 'I:VT002', 'I:VT003', 'R:VT001',
                              'R:VT002', 'R:VT003']),
    (['{I,R}:VT001', 'I:VT{001..002}'], [
     'I:VT001', 'R:VT001', 'I:VT001', 'I:VT002']),
    (['AB}C{D'], ['ABCD']),
    (['001..002'], ['001', '002']),
    (['A}BC,DE'], ['ABC', 'ADE']),
])
def test_generate(tests, expected):
    """
    Test the generate function.

    :param tests: Tests to run.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.generate(*tests))
    assert result == expected


@pytest.mark.parametrize('validatee,validator,expected', [
    (first_validation_file, 'I:VT{005..015}', []),
    (second_validation_file, 'I:VT{005..015}',
     ['ABCDEF', '1234', 'xYz']),
])
def test_verify(validatee, validator, expected):
    """
    Test the verify function.

    :param validatee: File to validate.
    :param validator: Validator.
    :param expected: Expected result.
    :param comparator: Comparator function.
    """
    result = list(drf_generator.verify(validatee, validator))
    assert result == expected
