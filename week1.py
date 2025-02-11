# Warmups
def twosum(arr, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    If there are multiple answers, return the ones with the smaller first index and then smaller second index.
    If there is no answer, return [-1, -1]
    """
    return [-1, -1]


def foobarbaz(n):
    """This function returns a list of the numbers from 1 ... n,
    However, multiples of 3 will be replaced; the first one with 'foo', the second with 'bar', and the third with 'baz'.
    This pattern will repeat. For example, if n=10, the output will be:
    ['1', '2', 'foo', '4', '5', 'bar', '7', '8', 'baz', '10']
    """
    return []


def sentence_palindrome(sentence):
    """
    Return true if the sentence is a palindrome. Ignore case, spaces, and punctuation.
    Hint: you can import the `string` module and `string.punctuation` to get a list of punctuation characters to ignore.
    """
    return False


def dyslexic_palindrome(word):
    """
    Return true if the input word is a palindrome. However, the letters d, p, b, and q are considered interchangeable.
    """
    return False


def local_minimums(arr):
    """
    Given an array of integers, return a list of indexes the local minimums.
    A local minimum is a number which is less than its neighbors.
    """
    return []

# Now that you're warmed up

def count_clumps(arr):
    """
    Return the number of clumps in the input list.
    A clump is a series of 2 or more adjacent elements of the same value.
    """
    return 0


def zero_matrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
    The matrix is passed as a list of lists, e.g:
    [   [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    DO NOT modify the original matrix, instead return a new matrix.
    Be careful when creating the new matrix - there are subtleties about copying lists in Python.
    I would suggest making a blank matrix of the same size as the input matrix, then modifying it.
    Or create the new matrix as you go along.
    Hint: Algorithm should be O(rows*columns) - try to avoid brute forcing.
    Hint: An empty matrix will be passed in as [[]]
    """
    return [[]]


def is_anagram(s1, s2):
    """
    Return True if the two input strings are anagrams of each other, False otherwise.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once. Ignore punctuation and capitalization.

    Reminder: Strings are just a collection of characters. Maybe thinking about them like a list will help.
    """
    return False