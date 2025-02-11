import week1
import unittest

import unittest


# Add your own test cases to the appropriate classes to test edge cases


class TwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertListEqual(week1.twosum([2, 7, 11, 15], 9), [0, 1])
    def test_no_answer(self):
        self.assertListEqual(week1.twosum([2, 7, 11, 15], 10), [-1, -1])

class FooBarBaz(unittest.TestCase):
    def test_foobarbaz(self):
        self.assertListEqual(week1.foobarbaz(10), [1, 2, 'foo', 4, 5, 'bar', 7, 8, 'baz', 10])

class SentencePalindrome(unittest.TestCase):
    def test_sentence_palindrome(self):
        self.assertTrue(week1.sentence_palindrome('A man, a plan, a canal, Panama'))

    def test_sentence_palindrome2(self):
        self.assertTrue(week1.sentence_palindrome('Was it a car or a cat I saw?'))

def test_false(self):
    self.assertFalse(week1.sentence_palindrome('hello world'))

class DyslexicPalindrome(unittest.TestCase):
    def test_dyslexic_palindrome(self):
        self.assertTrue(week1.dyslexic_palindrome('dab'))
        self.assertTrue(week1.dyslexic_palindrome('pad'))


class LocalMinimums(unittest.TestCase):
    def test_local_minimums(self):
        self.assertListEqual(week1.local_minimums([1, 2, 3, 4, 5]), [0])
        self.assertListEqual(week1.local_minimums([1, 2, 1, 4, 5]), [0, 2])


class CountClumps(unittest.TestCase):
    def test_count_clumps(self):
        self.assertEqual(week1.count_clumps([1, 2, 2, 3, 4, 4]), 2)

class ZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        self.assertListEqual(week1.zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]), [[1, 0, 3], [0, 0, 0], [7, 0, 9]])
    def test_not_modified(self):
        matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        week1.zero_matrix(matrix)
        self.assertListEqual(matrix, [[1, 2, 3], [4, 0, 6], [7, 8, 9]])


class IsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(week1.is_anagram('listen', 'silent'))
        self.assertFalse(week1.is_anagram('hello', 'world'))


if __name__ == '__main__':
    unittest.main()
