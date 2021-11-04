#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import drf_generator

# Unit tests for DRF Generator of extended expressions
class TestDRFGenerator(unittest.TestCase):

    def test_char_rangeA_F(self):
        expected = ['A', 'B', 'C', 'D', 'E', 'F']
        i = 0
        for result in drf_generator.char_range('A', 'F'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_char_range1_6(self):
        expected = ['1', '2', '3', '4', '5', '6']
        i = 0
        for result in drf_generator.char_range('1', '6'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_token_range1_6(self):
        expected = [1, 2, 3, 4, 5, 6]
        i = 0
        for result in drf_generator.token_range('1', '6'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_token_range001_006(self):
        expected = ['001', '002', '003', '004', '005', '006']
        i = 0
        for result in drf_generator.token_range('001', '006'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_token_range008_012(self):
        expected = ['008', '009', '010', '011', '012']
        i = 0
        for result in drf_generator.token_range('008', '012'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_token_range000998_001002(self):
        expected = ['000998', '000999', '001000', '001001', '001002']
        i = 0
        for result in drf_generator.token_range('000998', '001002'):
            self.assertEqual(expected[i], result)
            i += 1

    def test_generate_list_of_stringsI_R(self):
        result = drf_generator.generate("{I,R}:VT001")
        expected = ["I:VT001", "R:VT001"]

        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_list_of_stringsA_D(self):
        result = drf_generator.generate("{A,B,C,D}:VT001")
        expected = ["A:VT001", "B:VT001", "C:VT001", "D:VT001"]

        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_list_of_strings_empty(self):
        result = drf_generator.generate("I{}:VT001")
        # TODO should this be the expected value?
        expected = ["I:VT001"]

        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_range001_002(self):
        result = drf_generator.generate("I:VT{001..002}")
        expected = ["I:VT001", "I:VT002"]

        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_range005_015(self):
        result = drf_generator.generate("I:VT{005..015}")
        expected = ["I:VT005", "I:VT006", "I:VT007", "I:VT008", "I:VT009",
                    "I:VT010", "I:VT011", "I:VT012", "I:VT013", "I:VT014",
                    "I:VT015"]

        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_range_reverse(self):
        result = drf_generator.generate("I:VT{003..001}")
        # TODO should empty be expected?
        expected = []
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_list_and_range(self):
        result = drf_generator.generate("{I,R}:VT{001..03}")
        expected = ["I:VT001", "I:VT002", "I:VT003", "R:VT001", "R:VT002",
                    "R:VT003"]
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_generate_nested(self):
        result = drf_generator.generate("{I,R}:VT001", "I:VT{001..002}")
        expected = ["I:VT001", "R:VT001", "I:VT001", "I:VT002"]
        self.assertEqual(len(result), len(expected))
        self.assertListEqual(result, expected)

    def test_validate1(self):
        result = drf_generator.verify(
            "test/test_validate1.txt", "I:VT{005..015}")
        expected = True
        self.assertEqual(result, expected)

    def test_validate2(self):
        result = drf_generator.verify(
            "test/test_validate2.txt", "I:VT{005..015}")
        expected = ["ABCDEF", "1234", "xYz"]
        self.assertEqual(result, expected)

    def test_invalid_string1(self):
        result = drf_generator.generate("AB}C{D")
        # TODO should this be the expected?
        expected = ["ABCD"]
        self.assertEqual(expected, result)

    def test_invalid_string2(self):
        result = drf_generator.generate("001..002")
        # TODO should this be the expected?
        expected = ["001", "002"]
        self.assertEqual(expected, result)

    def test_invalid_string3(self):
        result = drf_generator.generate("A}BC,DE")
        # TODO should this be the expected?
        expected = ["ABC", "ADE"]
        self.assertEqual(expected, result)
