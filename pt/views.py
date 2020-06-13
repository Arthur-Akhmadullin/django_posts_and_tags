from django.shortcuts import render
from .models import Post

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'pt/index.html', {'posts': posts})
	
def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'pt/post_detail.html', {'post': post})