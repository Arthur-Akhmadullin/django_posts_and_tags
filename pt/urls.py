from django.urls import path
from .views import *

'''
Вместо метода post_detail установлен PostDetail.as_view()
Вместо метода tag_detail установлен TagDetail.as_view()
'''

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
	path('tags/', tags_list, name='tags_list_url'),
	path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
	path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
]