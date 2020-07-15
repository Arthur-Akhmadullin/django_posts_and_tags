from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q


def posts_list(request):
	search_query = request.GET.get('search', '')
	if search_query:
		posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
	else:
		posts = Post.objects.all()
	
		
	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', 1) #page - параметр get-запроса в адресной строке, 1 - ззначение по-умолчанию, на тот случай, если нужного значения page не существует (чтобы не возбуждать исключение)
	page = paginator.get_page(page_number)
	
	is_paginated = page.has_other_pages()
	
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''
		
	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url=''
		
	context = {
		'page_object': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}
	
	return render(request, 'pt/index.html', context=context)
	

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

		
class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
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
	raise_exception = True
	
	
class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'pt/post_update_form.html'
	raise_exception = True
	#def get(self, request, slug):
		#post = Post.objects.get(slug__iexact=slug)
		#bound_form = PostForm(instance=post)
		#return render(request, 'pt/post_update_form.html', {'form': bound_form, 'post': post})
		
	#def post(self, request, slug):
		#post = Post.objects.get(slug__iexact=slug)
		#bound_form = PostForm(request.POST, instance=post)
		
		#if bound_form.is_valid():
			#new_post = bound_form.save()
			#return redirect(new_post)
		#return render(request, 'pt/post_update_form.html', {'form': bound_form, 'post': post})
		
		
class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'pt/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exception = True
	#def get(self, request, slug):
		#post = Post.objects.get(slug__iexact=slug)
		#return render(request, 'pt/post_delete_form.html', {'post': post})
		
	#def post(self, request, slug):
		#post = Post.objects.get(slug__iexact=slug)
		#post.delete()		
		#return redirect(reverse('posts_list_url'))
		
	
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
	

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
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
	raise_exception = True
	
	
class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'pt/tag_update_form.html'
	raise_exception = True
	#def get(self, request, slug):
		#tag = Tag.objects.get(slug__iexact=slug)
		#bound_form = TagForm(instance=tag)
		#return render(request, 'pt/tag_update_form.html', {'form': bound_form, 'tag': tag})
		
	#def post(self, request, slug):
		#tag = Tag.objects.get(slug__iexact=slug)
		#bound_form = TagForm(request.POST, instance=tag)
		
		#if bound_form.is_valid():
			#new_tag = bound_form.save()
			#return redirect(new_tag)
		#return render(request, 'pt/tag_update_form.html', {'form': bound_form, 'tag': tag})
		
		
class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'pt/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exception = True
	#def get(self, request, slug):
		#tag = Tag.objects.get(slug__iexact=slug)
		#return render(request, 'pt/tag_delete_form.html', {'tag': tag})
		
	#def post(self, request, slug):
		#tag = Tag.objects.get(slug__iexact=slug)
		#tag.delete()		
		#return redirect(reverse('tags_list_url'))
	
	