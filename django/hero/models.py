from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Hero(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cta_link = models.URLField()
    cta_text = models.CharField(max_length=200)

    def __str__(self):
        return self.title
