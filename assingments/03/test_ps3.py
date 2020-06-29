import unittest
from ps3a import countSubStringMatch, countSubStringMatchRecursive

class TestPS3(unittest.TestCase):

  def test_countSubStringMatch(self):
    result = countSubStringMatch("qwertyqwertyqwertyqwertyqwerty", "ert")
    self.assertEqual(result, 5)
    result = countSubStringMatch("qwertyqwertyqwertyqwertyqwerty", "dfg")
    self.assertEqual(result, 0)

  def test_countSubStringMatchRecursive(self):
    result = countSubStringMatchRecursive("qwertyqwertyqwertyqwertyqwerty", "ert")
    self.assertEqual(result, 5)
    result = countSubStringMatchRecursive("qwertyqwertyqwertyqwertyqwerty", "hjkl")
    self.assertEqual(result, 0)


if __name__ == '__main__':
  unittest.main()