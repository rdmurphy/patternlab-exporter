from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Feature(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    url = models.SlugField()
    img_src = models.ImageField(upload_to='features')
    img_alt = models.CharField(max_length=200)

    def __str__(self):
        return self.title
