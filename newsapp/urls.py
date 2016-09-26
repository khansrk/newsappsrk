from django.conf.urls import url #for handling urls
from . import views,auth #from local module import views
urlpatterns = [  #list of urls

    url(r'^$', views.articles_list,name='articles_list'),
    url(r'^feeds/new', views.new_feed, name='feed_new'),
    url(r'^feeds/', views.feeds_list,name='feeds_list'),
    url(r'^login/', auth.login, name = 'login'),
    url(r'^logout/', auth.logout, name = 'logout'),
    url(r'^register/', auth.register, name = 'register'),
 ]
