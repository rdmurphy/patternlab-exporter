from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from markupfield.fields import MarkupField

from django.utils import timezone


# Create your models here.
@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField()
    excerpt = MarkupField(markup_type='markdown')
    content = MarkupField(markup_type='markdown')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
