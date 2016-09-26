from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import feedparser
import datetime

# Create your views here.

def articles_list(request):
    articles = Article.objects.all()

    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]

    return render(request, 'newsapp/articles_list.html', {'rows': rows})

@login_required
def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'newsapp/feeds_list.html', {'feeds': feeds})

@login_required
def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

                # set some fields
                feed.title = feedData.feed.title
                feed.save()

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    article.save()

            return redirect('newsapp.views.feeds_list')
    else:
        form = FeedForm()
    return render(request, 'newsapp/new_feed.html', {'form': form})
