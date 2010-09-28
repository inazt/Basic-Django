from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from bsc.news.models import News

def index(request):
    news = News.objects.all()
    context = RequestContext(request, {'news': news})

    return render_to_response('homepage/index.html', {'news': news}, context); 
   
