from django.db import models
from taggit.managers import TaggableManager

class Quote(models.Model):
	content = models.TextField(blank=True)
	tags = TaggableManager()
	timestamp = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
	reported = models.BooleanField(default=False)
	notes = models.TextField(blank=True)

	def __str__(self):
		return '#' + str(self.id) + ': ' + self.content[:100].strip() + ('...' if len(self.content) > 100 else '')

class Vote(models.Model):
	ip = models.GenericIPAddressField()
	useragent = models.TextField()
	value = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

	def __str__(self):
		return ('+' if self.value >= 0 else '') + str(self.value) + ' #' + str(self.quote.id)

class News(models.Model):
	author = models.TextField()
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'news'

	def __str__(self):
		return self.content[:100].strip() + ('...' if len(self.content) > 100 else '')