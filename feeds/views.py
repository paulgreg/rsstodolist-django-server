from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.utils import timezone

import logging

from models import FeedEntry
from converter import Converter
from urlfetcher import UrlFetcher
from feedNameCleaner import FeedNameCleaner
from limitParser import LimitParser


def index(request):
  feedNameCleaner = FeedNameCleaner()
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  if not name:
    return renderHome(request)
  else:
    limitParser = LimitParser()
    limit = limitParser.parse(request.GET.get('limit') or request.GET.get('l'))
    return renderRss(request, name, limit)


def renderHome(request):
  try:
    urlFetcher = UrlFetcher()
    random_url = urlFetcher.fetch('http://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=rss', '(?<=<link>)http://en.wikipedia.org/w/index.php?[^&]*')
  except Exception, err:
    logging.exception('Error while fetching example URL:')
    random_url = 'http://www.google.com/'
  
  context = { 'random_url': random_url }
  return render(request, 'index.html', context)


def renderRss(request, name, limit):
  feeds = FeedEntry.objects.filter(name=name).order_by('-creation_date')[:limit]
  context = { 'name': name, 'feeds': feeds }
  return render(request, 'rss.xml', context,  content_type='text/xml')


def add(request): 
  feedNameCleaner = FeedNameCleaner()
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  url = request.GET.get('url') or request.GET.get('u')
  if not name or not url:
    return HttpResponseRedirect('/')
  else:
    title  = request.GET.get('title') or request.GET.get('t')
    description = request.GET.get('description') or request.GET.get('d')
    addUrl(url, name, title, description)

    return HttpResponseRedirect('/?name=' + name)


def addUrl(url, name, title, description):
  converter = Converter()
  formatedUrl = url.replace('&', '&amp;')

  if name == 'somename' and not url.startswith('http://en.wikipedia.org/'):
    return # Spam protection for default feed name

  lastFeedEntries = FeedEntry.objects.filter(name=name).order_by('-creation_date')

  if len(lastFeedEntries) == 0 or formatedUrl != lastFeedEntries[0].url: # Do not add same URL twice !

    feedentry = FeedEntry(url=formatedUrl, name=name, creation_date=timezone.now())
    feedentry.description = converter.convert(description)

    if not title:
        try:
          urlFetcher = UrlFetcher()
          title = urlFetcher.fetch(url, '(?<=<(title|TITLE)>)[^<|^\r|^\n]*')
        except Exception, err:
          logging.exception('Error while fetching page title:')
          feedentry.title = feedentry.url

    feedentry.title = converter.convert(title)

    if not feedentry.title:
        feedentry.title = feedentry.url

    feedentry.save()

def delete(request): 
  feedNameCleaner = FeedNameCleaner()
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  if not name:
    return renderHome(request)
  else:
    url = request.GET.get('url') or request.GET.get('u')

    if url:
      deleteUrl(url, name)

    return HttpResponseRedirect('/?name=' + name)


def deleteUrl(url, name):
  formatedUrl = url.replace('&', '&amp;')

  feed = FeedEntry.objects.filter(name=name, url=url).order_by('-creation_date')

  if len(feed) >= 1:
    feed[0].delete()

