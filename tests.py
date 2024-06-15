import unittest

from contest_52598_a import remove_duplicates
from contest_52598_b import define_insert_index
from contest_52599_a import is_regular_mountain
from contest_52599_c import is_correct_sequence
from contest_52718_a import count_numbers_less_specified
from contest_52718_b import max_substring_len
from contest_52720_a import platforms_needed


class ContestTestCase(unittest.TestCase):

    def test_remove_duplicates(self):
        data = (
            ([1, 1, 2], [1, 2, '_']),
            (
                [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
                [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
            ),
            ([0, 3, 5, 11, 11], [0, 3, 5, 11, '_']),
        )
        for arr, expected in data:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(remove_duplicates(arr), expected)

    def test_define_insert_index(self):
        data = (
            ([1, 3, 5, 6], 5, 2),
            ([1, 5, 10, 11], 2, 1),
            ([3, 7, 10, 20, 23], 25, 5),
        )
        for arr, value, expected in data:
            with self.subTest(arr=arr, value=value, expected=expected):
                self.assertEqual(define_insert_index(arr, value), expected)

    def test_is_regular_mountain(self):
        data = (
            ([2, 1, 3, 5, 8], False),
            ([3, 5, 5], False),
            ([0, 3, 2, 1], True),
            ([1, 2], False),
            ([5, 4, 3, 2, 1], False),
        )
        for arr, expected in data:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(is_regular_mountain(arr), expected)

    def test_is_correct_bracket_sequence(self):
        data = (
            ('()', True),
            ('({[]})', True),
            ('({[]})([])', True),
            ('{[}', False),
        )
        for string, expected in data:
            with self.subTest(string=string, expected=expected):
                self.assertEqual(is_correct_sequence(string), expected)

    def test_count_numbers_less_specified(self):
        data = (
            ([6, 5, 4, 8], [2, 1, 0, 3]),
            ([7, 7, 7, 7], [0, 0, 0, 0]),
            ([1, 7, 3, 7, 6], [0, 3, 1, 3, 2]),
        )
        for arr, expected in data:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(count_numbers_less_specified(arr), expected)

    def test_max_substring_len(self):
        data = (
            ('abcabcbb', 3),
            ('bbbbb', 1),
        )
        for string, expected in data:
            with self.subTest(string=string, expected=expected):
                self.assertEqual(max_substring_len(string), expected)

    def test_platforms_needed(self):
        data = (
            ([1, 2], 3, 1),
            ([3, 2, 2, 1], 3, 3),
            ([3, 5, 3, 4], 5, 4),
        )
        for arr, limit, expected in data:
            with self.subTest(arr=arr, limit=limit, expected=expected):
                self.assertEqual(platforms_needed(arr, limit), expected)


if __name__ == '__main__':
    unittest.main()
