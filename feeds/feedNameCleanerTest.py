# -*- coding: utf-8 -*-

import unittest
from feedNameCleaner import FeedNameCleaner

class TestFeedNameCleaner(unittest.TestCase):

   def testCleanNothing(self):
     assert cleaner.clean('') == ''

   def testCleanSpaces(self):
     assert cleaner.clean(' spaces ') == 'spaces'

   def testCleanMoreSpaces(self):
     assert cleaner.clean(' abc  def ') == 'abcdef'

   def testCleanStrangeChar(self):
     assert cleaner.clean('abc à&é" DEF') == 'abcDEF'

   def testCleanButSomeChar(self):
     assert cleaner.clean('a-c-z') == 'a-c-z'


if __name__=="__main__":
   cleaner = FeedNameCleaner()
   unittest.main()

