# source: https://docs.python.org/3/library/unittest.html

import unittest
import insertionsort as IS

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestSorts(unittest.TestCase):
    
  def test_empty(self):
      self.assertEqual(IS.insertionSort([]),[])

if __name__ == '__main__':
    unittest.main()