# -*- coding: utf-8 -*-

import unittest
from converter import Converter

class TestConverter(unittest.TestCase):

   def testConvertNothing(self):
     assert converter.convert('') == ''

   def testConvertSomethingSimple(self):
     assert converter.convert('A simple url: www.google.com') == 'A simple url: www.google.com'

   def testConvertHtmlName(self):
     assert converter.convert('Gr&eacute;gory Paul') == 'Grégory Paul'.decode('utf8')

   # Title from http://www.necdisplay.com/NewTechnologies/CurvedDisplay/
   def testConvertRaquo(self):
     assert converter.convert('NEC Display Solutions &raquo; News & Media &raquo; Media Coverage') == 'NEC Display Solutions \' News and Media \' Media Coverage'

   # Title from http://tempsreel.nouvelobs.com/actualites/societe/20091013.OBS4458/
   def testConvertAccents(self):
     assert converter.convert('Trois cas de gale ont été signalés à l\'Elysée, Soci&eacute;t&eacute;') == 'Trois cas de gale ont été signalés à l\'Elysée, Société'.decode('utf8')

   # Title from http://stackoverflow.com/questions/1594261/
   def testConvertTags(self):
     assert converter.convert('Remove visability on &lt;li&gt; tags except (this) on hover in a menu') == 'Remove visability on {li} tags except (this) on hover in a menu'

   def testConvertTags(self):
     assert converter.convert('multi\r\nline') == 'multi line'

   def testConvertTags(self):
     assert converter.convert('tab\tother tab') == 'tab other tab'

   def testConvertAccents(self):
     assert converter.convert('test de commentaire avec accent : &eacute;&egrave;&ecirc;&icirc;&ocirc;') == 'test de commentaire avec accent : éèêîô'.decode('utf8')

   # Title from https://hacks.mozilla.org/2017/02/a-crash-course-in-just-in-time-jit-compilers/
   def testConvertAccents(self):
     assert converter.convert('A crash course in just-in-time (JIT) compilers &#x2605; Mozilla Hacks &#8211;') == 'A crash course in just-in-time (JIT) compilers  Mozilla Hacks –'.decode('utf8')

   def testConvertAccents(self):
       assert converter.convert('Meyclub - Créateur de loisirs') == 'Meyclub - Créateur de loisirs'.decode('utf8')

if __name__=="__main__":
   converter = Converter()
   unittest.main()

