import unittest
from limitParser import LimitParser

class TestLimitParser(unittest.TestCase):

   def testParseEmptyStringShouldReturnDefaultLimitValue(self):
     assert parser.parse('') == 25

   def testParseStringWithSpacesShouldReturnDefaultLimitValue(self):
     assert parser.parse(' spaces ') == 25

   def testParseASimpleNumberShouldWork(self):
     assert parser.parse('12') == 12

   def testParseASimpleNumberWithSpacesShouldWork(self):
     assert parser.parse(' 13 ') == 13

   def testParseAFloatNumberShouldReturnDefaultLimitValue(self):
     assert parser.parse('16.45') == 25
     assert parser.parse('12,45') == 25

   def testParseZeroShouldRetunDefaultLimitValue(self):
     assert parser.parse('0') == 25

   def testParseNegativeNumberShouldRetunDefaultLimitValue(self):
     assert parser.parse('-2') == 25

   def testParseNumberSuperiorToUpperBoundShouldRetunMaxValue(self):
     assert parser.parse('154') == 100


if __name__=="__main__":
   parser = LimitParser()
   unittest.main()

