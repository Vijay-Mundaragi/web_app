from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User #default user model provided by django 

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	#after creating a post, we want to go to post-detail page of post which is just created
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})