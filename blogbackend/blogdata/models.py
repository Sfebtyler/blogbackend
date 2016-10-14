from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Post(models.Model):

    createdon = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    posttext = models.CharField(max_length=10000, blank=True, default='')
    postimage = models.ImageField(upload_to = 'images/', default='images/None/')


    class Meta:
        ordering = ('createdon',)


