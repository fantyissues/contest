import unittest

from contest_52598_a import remove_duplicates
from contest_52598_b import define_insert_index


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


if __name__ == '__main__':
    unittest.main()
