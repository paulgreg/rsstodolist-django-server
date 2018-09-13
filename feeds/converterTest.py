# coding: utf8
# -*- coding: utf-8 -*-

import unittest
from converter import Converter

class TestConverter(unittest.TestCase):

   def testConvertNothing(self):
     assert converter.convert('') == u''

   def testConvertSomethingSimple(self):
     assert converter.convert('A simple url: www.google.com') == u'A simple url: www.google.com'

   def testConvertHtmlName(self):
     assert converter.convert('Gr&eacute;gory Paul') == u'Grégory Paul'

   # Title from http://www.necdisplay.com/NewTechnologies/CurvedDisplay/
   def testConvertRaquo(self):
     assert converter.convert('NEC Display Solutions &raquo; News & Media &raquo; Media Coverage') == u'NEC Display Solutions » News & Media » Media Coverage'

   def testConvertAccent(self):
     assert converter.convert('Meyclub - Créateur') == u'Meyclub - Créateur'

   def testConvertAccentStringEncoded(self):
     assert converter.convert('Soci&eacute;t&eacute;') == u'Société'

   def testConvertAccentNumberEncoded(self):
     assert converter.convert('Pot de d&#233;part'.encode('iso-8859-1')) == u'Pot de départ'

   # Title from http://stackoverflow.com/questions/1594261/
   def testConvertTag(self):
     assert converter.convert('Remove visability on &lt;li&gt;') == u'Remove visability on {li}'

   def testConvertLineReturn(self):
     assert converter.convert('multi\r\nline') == u'multi line'

   def testConvertTab(self):
     assert converter.convert('tab\tother tab') == u'tab other tab'

   def testConvertMoreAccents(self):
     assert converter.convert('test de commentaire avec accent : &eacute;&egrave;&ecirc;&icirc;&ocirc;') == u'test de commentaire avec accent : éèêîô'

   # Title from https://hacks.mozilla.org/2017/02/a-crash-course-in-just-in-time-jit-compilers/
   def testConvertStar(self):
     assert converter.convert('A crash course in just-in-time (JIT) compilers &#x2605; Mozilla Hacks &#8211;') == u'A crash course in just-in-time (JIT) compilers ★ Mozilla Hacks –'

   def testConvertUnicode(self):
     assert converter.convert(u'é') == u'é'


if __name__=="__main__":
   converter = Converter()
   unittest.main()

