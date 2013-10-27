from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

import logging

from models import FeedEntry
from urlfetcher import UrlFetcher
from feedNameCleaner import FeedNameCleaner
from limitParser import LimitParser

from storeActions import StoreActions


feedNameCleaner = FeedNameCleaner()
urlFetcher = UrlFetcher()
limitParser = LimitParser()
storeActions = StoreActions()


def index(request):
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  if not name:
    return renderHome(request)
  else:
    limit = limitParser.parse(request.GET.get('limit') or request.GET.get('l'))
    return renderRss(request, name, limit)


def renderHome(request):
  try:
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
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  url = request.GET.get('url') or request.GET.get('u')
  if not name or not url:
    return HttpResponseRedirect('/')
  else:
    title  = request.GET.get('title') or request.GET.get('t')
    description = request.GET.get('description') or request.GET.get('d')
    storeActions.addUrl(url, name, title, description)

    return HttpResponseRedirect('/?name=' + name)


def delete(request): 
  name = feedNameCleaner.clean(request.GET.get('name') or request.GET.get('n'))
  if not name:
    return renderHome(request)
  else:
    url = request.GET.get('url') or request.GET.get('u')

    if url:
      storeActions.deleteUrl(url, name)

    return HttpResponseRedirect('/?name=' + name)


