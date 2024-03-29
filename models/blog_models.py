from django.db import models

# Create your models here.

class news(models.Model):
    class Meta:
        app_label = 'blog'

    title = models.TextField(max_length=100)
    content = models.TextField(max_length=250)
    author = models.TextField(max_length = 250)
    description = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.title