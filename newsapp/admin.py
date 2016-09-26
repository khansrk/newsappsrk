from django.contrib import admin
from newsapp.models import Feed,Article

class FeedAdmin(admin.ModelAdmin):
    list_display = ('title','status',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','feed','description','publication_date',)

admin.site.register(Feed,FeedAdmin)
admin.site.register(Article,ArticleAdmin)
