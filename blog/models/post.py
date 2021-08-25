from django.db import models

class Post(models.Model):

	title = models.CharField(max_length = 50)
	conteudo = models.TextField(max_length = 280)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	file = models.FileField(upload_to = 'uploads/')
	



	def __str__(self):
		return self.title


	class Meta:
		app_label = "blog"
		verbose_name = "Post"
		verbose_name_plural = "Posts"


