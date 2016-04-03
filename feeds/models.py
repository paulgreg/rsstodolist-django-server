from django.db import models

class FeedEntry(models.Model):
  name = models.CharField(max_length=20)
  url = models.CharField(max_length=512)
  title = models.CharField(max_length=255,null=True)
  creation_date = models.DateTimeField(auto_now=True)
  description = models.TextField(null=True)

  def __unicode__(self):
    return self.url
