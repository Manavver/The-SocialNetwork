from django.shortcuts import render
from django.utils import timezone
from .models import Article

def posts(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'socialNetwork/posts.html', {'posts': posts})
