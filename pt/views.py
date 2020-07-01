from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


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

		
class PostCreate(ObjectCreateMixin, View):
	#def get(self, request):
		#form = PostForm()
		#return render(request, 'pt/post_create.html', {'form': form})
		
	#def post(self, request):
		#bound_form = PostForm(request.POST)
		
		#if bound_form.is_valid():
			#new_post = bound_form.save()
			#return redirect(new_post)
		#return render(request, 'pt/post_create.html', {'form': bound_form})
	model_form = PostForm
	template = 'pt/post_create.html'
		
	
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
	

class TagCreate(ObjectCreateMixin, View):
	#def get(self, request):
		#form = TagForm()
		#return render(request, 'pt/tag_create.html', {'form': form})
		
	#def post(self, request):
		#bound_form = TagForm(request.POST)
		
		#if bound_form.is_valid():
			#new_tag = bound_form.save()
			#return redirect(new_tag)
		#return render(request, 'pt/tag_create.html', {'form': bound_form})
	model_form = TagForm
	template = 'pt/tag_create.html'
	
	