from django.db import models

# Create your models here.

class Topic(models.Model):
	"""my learning topic"""
	text = models.CharField(max_length=100)

	def __str__(self):
		"""return the topic's text"""
		return self.text

class Article(models.Model):
	"""my learning ariticle"""
	pub_date = models.DateField(auto_now_add=True)
	headline = models.CharField(max_length=200)
	content = models.TextField()
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

	def __str__(self):
		"""return the article's content"""
		if len(self.content) < 100:
			return self.content
		else:
			return self.content[:100] + '......'
