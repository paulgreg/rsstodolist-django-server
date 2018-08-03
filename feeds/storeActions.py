from models import FeedEntry
from converter import Converter
from urlfetcher import UrlFetcher

import logging

class StoreActions():

  def __init__(self):
    self.converter = Converter()
    self.urlFetcher = UrlFetcher()

  def addUrl(self, url, name, title, description):
    if name == 'somename' and not url.startswith('http://en.wikipedia.org/'):
      return # Spam protection for default feed name

    lastFeedEntries = FeedEntry.objects.filter(name=name).order_by('-creation_date')

    if len(lastFeedEntries) == 0 or url != lastFeedEntries[0].url: # Do not add same URL twice !

      feedentry = FeedEntry(url=url, name=name)
      feedentry.description = self.converter.convert(description)

      if not title:
          try:
            title = self.urlFetcher.fetch(url, '(?<=<(title|TITLE)>)[^<|^\r|^\n]*')
          except Exception, err:
            logging.exception('Error while fetching page title:')
            feedentry.title = feedentry.url

      feedentry.title = self.converter.convert(title)

      if not feedentry.title:
          feedentry.title = feedentry.url

      feedentry.save()


  def deleteUrl(self, url, name):
    feed = FeedEntry.objects.filter(name=name, url=url).order_by('-creation_date')

    if len(feed) >= 1:
      feed[0].delete()

