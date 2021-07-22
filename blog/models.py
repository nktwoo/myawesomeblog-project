from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=30)
	date = models.DateTimeField()
	text = models.CharField(max_length=300)
	image = models.ImageField(upload_to='event_images/')