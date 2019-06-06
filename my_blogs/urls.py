"""my_blogs URLS"""

from django.urls import path,re_path

from . import views

urlpatterns = [
	#home page
	#path('',views.home,name='home'),
	re_path(r'^$',views.home,name='home'),

	#path('topics',views.topics,name='topics')
	re_path(r'^topics/$',views.topics,name='topics')

]


