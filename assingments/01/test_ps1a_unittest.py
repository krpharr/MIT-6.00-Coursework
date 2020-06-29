import unittest
from ps1a import isPrime

class TestPS1A(unittest.TestCase):

  def test_isPrime(self):
    result = isPrime(199)
    self.assertEqual(result, 1)

  def test_isPrime(self):
    result = isPrime(25)
    self.assertEqual(result, 0)

if __name__ == '__main__':
  unittest.main()