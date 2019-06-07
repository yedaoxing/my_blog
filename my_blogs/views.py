from django.shortcuts import render

from .models import Topic,Article

def build_article(headline,article):
	"""build a headline-article dic"""
	dic = {}
	dic['headline'] = headline
	dic['article'] = article
	return dic

# Create your views here.
def home(request):
	"""home page"""
	topics = Topic.objects.all()
	#topics = topics[:-1]
	html_content = {'topics':topics}
	return render(request,'my_blogs/home.html',html_content)


def topics(request):
	"""show topics"""
	topics = Topic.objects.all()
	html_content = {'topics':topics}
	return render(request,'my_blogs/topics.html',html_content)


def topic(request,topic_id):
	"""show the request topic"""
	topic = Topic.objects.get(id=int(topic_id))
	articles = topic.article_set.all()
	html_content = {'topic':topic,'articles':articles}
	return render(request,'my_blogs/topic.html',html_content)

def article(request,topic_id,article_id):
	#show article
	topic = Topic.objects.get(id=int(topic_id))
	article = topic.article_set.get(id=int(article_id))
	html_content = {'topics':topic,'article':article}
	return render(request,'my_blogs/article.html',html_content)




