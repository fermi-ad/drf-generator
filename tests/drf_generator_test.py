#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pathlib import Path

import drf_generator

parent_path = Path(__file__).parent
first_validation_file = parent_path.joinpath('test_validate1.txt')
second_validation_file = parent_path.joinpath(
    'test_validate2.txt')

# Unit tests for DRF Generator of extended expressions
class TestDRFGenerator(unittest.TestCase):

    def test_char_rangeA_F(self):
        expected = ['A', 'B', 'C', 'D', 'E', 'F']
        result = [x for x in drf_generator.char_range('A', 'F')]

        self.assertListEqual(expected, result)

    def test_char_rangeF_A(self):
        # expected = ['F', 'E', 'D', 'C', 'B', 'A']
        # Empty expected
        expected = []
        result = [x for x in drf_generator.char_range('F', 'A')]

        self.assertListEqual(expected, result)

    def test_char_range1_6(self):
        expected = ['1', '2', '3', '4', '5', '6']
        result = [x for x in drf_generator.char_range('1', '6')]

        self.assertListEqual(expected, result)

    def test_token_range1_6(self):
        expected = [1, 2, 3, 4, 5, 6]
        result = [x for x in drf_generator.token_range('1', '6')]

        self.assertListEqual(expected, result)

    def test_token_range6_1(self):
        #expected = [6, 5, 4, 3, 2, 1]
        # Empty expected
        expected = []
        result = [x for x in drf_generator.token_range('6', '1')]

        self.assertListEqual(expected, result)

    def test_token_rangeA_F(self):
        expected = ['A', 'B', 'C', 'D', 'E', 'F']
        result = [x for x in drf_generator.token_range('A', 'F')]

        self.assertListEqual(expected, result)

    def test_token_range001_006(self):
        expected = ['001', '002', '003', '004', '005', '006']
        result = [x for x in drf_generator.token_range('001', '006')]

        self.assertListEqual(expected, result)

    def test_token_range006_001(self):
        # expected = ['006', '005', '004', '003', '002', '001']
        # Empty expected
        expected = []
        result = [x for x in drf_generator.token_range('006', '001')]

        self.assertListEqual(expected, result)

    def test_token_range008_012(self):
        expected = ['008', '009', '010', '011', '012']
        result = [x for x in drf_generator.token_range('008', '012')]

        self.assertListEqual(expected, result)

    def test_token_range000998_001002(self):
        expected = ['000998', '000999', '001000', '001001', '001002']
        result = [x for x in drf_generator.token_range('000998', '001002')]

        self.assertListEqual(expected, result)

    def test_generate_list_of_stringsI_R(self):
        result = drf_generator.generate("{I,R}:VT001")
        expected = ["I:VT001", "R:VT001"]

        self.assertListEqual(result, expected)

    def test_generate_list_of_stringsA_D(self):
        result = drf_generator.generate("{A,B,C,D}:VT001")
        expected = ["A:VT001", "B:VT001", "C:VT001", "D:VT001"]

        self.assertListEqual(result, expected)

    def test_generate_list_of_strings_empty(self):
        result = drf_generator.generate("I{}:VT001")
        expected = ["I:VT001"]

        self.assertListEqual(result, expected)

    def test_generate_range001_002(self):
        result = drf_generator.generate("I:VT{001..002}")
        expected = ["I:VT001", "I:VT002"]

        self.assertListEqual(result, expected)

    def test_generate_range005_015(self):
        result = drf_generator.generate("I:VT{005..015}")
        expected = ["I:VT005", "I:VT006", "I:VT007", "I:VT008", "I:VT009",
                    "I:VT010", "I:VT011", "I:VT012", "I:VT013", "I:VT014",
                    "I:VT015"]

        self.assertListEqual(result, expected)

    def test_generate_range_reverse(self):
        result = drf_generator.generate("I:VT{003..001}")
        # TODO should empty be expected?
        expected = []
        self.assertListEqual(result, expected)

    def test_generate_list_and_range(self):
        result = drf_generator.generate("{I,R}:VT{001..003}")
        expected = ["I:VT001", "I:VT002", "I:VT003", "R:VT001", "R:VT002",
                    "R:VT003"]

        self.assertListEqual(result, expected)

    def test_generate_nested(self):
        result = drf_generator.generate("{I,R}:VT001", "I:VT{001..002}")
        expected = ["I:VT001", "R:VT001", "I:VT001", "I:VT002"]

        self.assertListEqual(result, expected)

    def test_validate1(self):
        result = drf_generator.verify(
            first_validation_file, "I:VT{005..015}")
        expected = True

        self.assertEqual(result, expected)

    def test_validate2(self):
        result = drf_generator.verify(
            second_validation_file, "I:VT{005..015}")
        expected = ["ABCDEF", "1234", "xYz"]

        self.assertEqual(result, expected)

    def test_invalid_string1(self):
        result = drf_generator.generate("AB}C{D")

        expected = ["ABCD"]
        # TODO fail this test when validation is implemented
        self.assertEqual(expected, result)

    def test_invalid_string2(self):
        result = drf_generator.generate("001..002")
        expected = ["001", "002"]

        self.assertEqual(expected, result)

    def test_invalid_string3(self):
        result = drf_generator.generate("A}BC,DE")
        # TODO fail this test when validation is implemented
        expected = ["ABC", "ADE"]

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
