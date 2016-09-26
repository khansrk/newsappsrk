from django.conf.urls import include, url
from django.contrib import admin
from newsapp import views,auth #from local module import views
urlpatterns = [
    url(r'^$', views.articles_list,name='articles_list'),
    url(r'^feeds/new', views.new_feed, name='feed_new'),
    url(r'^feeds/', views.feeds_list,name='feeds_list'),
    url(r'^login/', auth.login, name = 'login'),
    url(r'^logout/', auth.logout, name = 'logout'),
    url(r'^register/', auth.register, name = 'register'),
    url(r'^admin/', include(admin.site.urls)),
]
