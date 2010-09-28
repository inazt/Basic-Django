from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def news_list(request):
    news = News.objects.all()
    return render_to_response('homepage/index.html', {'NEWS': news}); 
