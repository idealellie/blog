from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)

    def __srt__(self):
        return self.title