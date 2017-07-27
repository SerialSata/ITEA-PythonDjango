from django.db import models
from laserapp.models import Laserapp
from accounts.models import User


class Comment(models.Model):
    product = models.ForeignKey(Laserapp)
    # author = models.CharField('Author name', help_text='Name of author', max_length=30, )
    author = models.ForeignKey(User)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
