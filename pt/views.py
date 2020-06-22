from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin


def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'pt/index.html', {'posts': posts})
	

'''
Функционал методов post_detail и tag_detail перенесен в классы PostDetail и TagDetail
'''	
#def post_detail(request, slug):
	#post = Post.objects.get(slug__iexact=slug)
	#return render(request, 'pt/post_detail.html', {'post': post})
	
class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'pt/post_detail.html'
	#def get(self, request, slug):
		#post = get_object_or_404(Post, slug__iexact=slug)
		#return render(request, 'pt/post_detail.html', {'post': post})
		
	
def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'pt/tags_list.html', {'tags': tags})


#def tag_detail(request, slug):
	#tag = Tag.objects.get(slug__iexact=slug)
	#return render(request, 'pt/tag_detail.html', {'tag': tag})
	
class TagDetail(ObjectDetailMixin, View):
	#def get(self, request, slug):
		#tag = get_object_or_404(Tag, slug__iexact=slug)
		#return render(request, 'pt/tag_detail.html', {'tag': tag})
	model = Tag
	template = 'pt/tag_detail.html'
	