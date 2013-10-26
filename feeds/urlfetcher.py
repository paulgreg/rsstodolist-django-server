import urllib2
import re

class UrlFetcher():

  def fetch(self, url, regexp):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    result = opener.open(url)

    if result.getcode() == 200:
      content = result.read()
      m = re.search(regexp, content)
      if m.group(0):
        return m.group(0)

    return null
