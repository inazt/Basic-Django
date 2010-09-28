from django.contrib import admin
from bsc.news.models import News

class NewsAdmin(admin.ModelAdmin): 
   list_display = ('title', 'created') 
admin.site.register(News, NewsAdmin)
