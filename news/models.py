from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'News'
