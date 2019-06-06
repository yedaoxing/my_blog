from django.shortcuts import render

from .models import Topic

def build_article(headline,article):
	"""build a headline-article dic"""
	dic = {}
	dic['headline'] = headline
	dic['article'] = article
	return dic

# Create your views here.
def home(request):
	"""home page"""
	query_topics = Topic.objects.all()
	topics = []
	for topic in query_topics:
		topics.append(topic.text)
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




