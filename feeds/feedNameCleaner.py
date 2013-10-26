import re

class FeedNameCleaner():

  def clean(self,nameToClean):
    # Remove everything (including space, accents) except letters, numbers and '-'
    if (nameToClean):
      return re.sub('[^A-Za-z0-9-]', '', nameToClean) 
    else:
      return ''
