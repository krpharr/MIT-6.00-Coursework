import unittest
from ps3a import countSubStringMatch, countSubStringMatchRecursive
from ps3b import subStringMatchExact

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

class TestPS3a(unittest.TestCase):

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

class TestPS3b(unittest.TestCase):

  def test_subStringMatchExact(self):
    print(target2, key12)
    result = subStringMatchExact(target2,key12)
    self.assertEqual(result, (4,18))

    print(target2, key11)
    result = subStringMatchExact(target2,key11)
    self.assertEqual(result, (0,4,8,12,18))

    print(target2, "key11")
    result = subStringMatchExact(target2,"key11")
    self.assertEqual(result, ())


if __name__ == '__main__':
  unittest.main()