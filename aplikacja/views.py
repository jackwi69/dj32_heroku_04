from django.shortcuts import render
from .models import Publication, Article

def index(request):
    context = {'index':'Index!'}
    return render(request, 'aplikacja/index.html', context)

def publish(request):
    pubs = Publication.objects.all()
    arts = Article.objects.all()
    context = {'pubs':pubs, 'arts':arts}
    return render(request, 'aplikacja/publication.html', context)
