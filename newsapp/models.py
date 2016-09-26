from django.db import models



STATUSES = (
    ('a','Active'),
    ('n','Inactive'),
    ('r','Rejected'),
)


    
class Feed(models.Model): #Feed is the parent class to fetch the url
    title = models.CharField(max_length=250)
    url = models.URLField()
    status = models.CharField(max_length = 1,choices=STATUSES)
    def __str__(self):
        return self.title


class Article(models.Model): #article is the sub class belongs to single feed
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=250)
    url = models.URLField()
    description = models.TextField()
    publication_date = models.DateTimeField()
    def __str__(self):
        return self.title
