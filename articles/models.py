from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	# add in thumbnail and the author later

#making a migration
#python manage.py makemigration

#migrating it
#python manage.py migrate

	def __str__(self):
		return self.title