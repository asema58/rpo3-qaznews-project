from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Advertisement
import random

def index(request):
    latest_posts = Post.objects.all()[:4]
    all_posts = list(Post.objects.all())
    random_posts = random.sample(all_posts, min(4, len(all_posts)))
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'latest_posts': latest_posts,
        'random_posts': random_posts,
        'ads': random_ads,
        'categories': categories,
    })

def all_news(request):
    posts = Post.objects.all()
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'all_news.html', {
        'posts': posts,
        'ads': random_ads,
        'categories': categories,
    })

def read_news(request, pk):
    post = get_object_or_404(Post, pk=pk)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)[:4]
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'read_news.html', {
        'post': post,
        'related_posts': related_posts,
        'ads': random_ads,
        'categories': categories,
    })

def news_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'news_by_category.html', {
        'category': category,
        'posts': posts,
        'ads': random_ads,
        'categories': categories,
    })

def search(request):
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'search.html', {
        'ads': random_ads,
        'categories': categories,
    })

def search_results(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query) if query else []
    ads = list(Advertisement.objects.all())
    random_ads = random.sample(ads, min(4, len(ads)))
    categories = Category.objects.all()
    return render(request, 'search_results.html', {
        'posts': posts,
        'query': query,
        'ads': random_ads,
        'categories': categories,
    })