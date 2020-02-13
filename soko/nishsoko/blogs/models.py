from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated']
    def __str__(self):
        return self.title