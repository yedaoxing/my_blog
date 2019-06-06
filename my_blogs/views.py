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
	query_topics = Topic.objects.all()
	topics = []
	for topic in query_topics:
		topics.append(topic.text)
	#topics = topics[:-1]
	html_content = {'topics':topics}
	return render(request,'my_blogs/topics.html',html_content)

def topic(request,topic_id):
	"""show the topic"""
	topic = Topic.objects.get(id=topic_id)
	query_articles = topic.article_set.all()
	headline_articles = []

	for article in query_articles:
		#build headline-article dic
		dic = build_article(article.headline,article.content)
		headline_articles.append(dic)

	html_content = {'topic':topic,'headline_articles':headline_articles}
	return render(request,'my_blogs/topic.html',html_content)



