import unittest
from ps2b import solve

class TestPS1A(unittest.TestCase):

  def test_solve_prob_1(self):
    result = solve(50)
    self.assertEqual(result, (2,2,1))

  def test_range(self):
    for i in range(6, 200):
      print(i, solve(i))    


if __name__ == '__main__':
  unittest.main()