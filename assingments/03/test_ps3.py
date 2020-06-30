import unittest
from ps3a import countSubStringMatch, countSubStringMatchRecursive
from ps3b import subStringMatchExact
from ps3c import constrainedMatchPair
from ps3d import subStringMatchExactlyOneSub 

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchOneSub(key,target):
  """search for all locations of key in target, with one substitution"""
  allAnswers = ()
  for miss in range(0,len(key)):
    # miss picks location for missing element
    # key1 and key2 are substrings to match
    key1 = key[:miss]
    key2 = key[miss+1:]
    #print 'breaking key',key,'into',key1,key2
    # match1 and match2 are tuples of locations of start of matches
    # for each substring in target
    match1 = subStringMatchExact(target,key1)
    match2 = subStringMatchExact(target,key2)
    # when we get here, we have two tuples of start points
    # need to filter pairs to decide which are correct
    filtered = constrainedMatchPair(match1,match2,len(key1))
    allAnswers = allAnswers + (filtered, )
    #print target
    #print 'match1',match1
    #print 'match2',match2
    #print 'possible matches for',key1,key2,'start at',filtered
  return allAnswers

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

class TestPS3c(unittest.TestCase):
  
  def test_subStringMatchOneSub(self):
    result = subStringMatchOneSub(key11,target1)
    self.assertEqual(result, ((0, 5, 15), (0, 5, 11, 15), (0, 5, 15)))

class TestPS3d(unittest.TestCase):
  
  def test_subStringMatchOneSub(self):
    result = subStringMatchOneSub(key11,target1)
    self.assertEqual(result, ((0, 5, 15), (0, 5, 11, 15), (0, 5, 15)))




  


if __name__ == '__main__':
  unittest.main()