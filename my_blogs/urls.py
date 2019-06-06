"""my_blogs URLS"""

from django.urls import path,re_path

from . import views

urlpatterns = [
	#home page
	#path('',views.home,name='home'),
	re_path(r'^$',views.home,name='home'),

	#all the topics
	#path('topics',views.topics,name='topics') why this sentences doesn't work?
	re_path(r'^topics/$',views.topics,name='topics'),

	#show the ask topic
	#re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
	re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic')

]


