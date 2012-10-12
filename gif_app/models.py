from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django.forms import ModelForm

class Gif(models.Model):
    title = models.CharField(max_length=30, default="Title")
    user = models.ForeignKey(User)
    file_path = models.FileField(upload_to=settings.MEDIA_ROOT+'gifs/')
    pub_date = models.DateTimeField('date posted')

class GifForm(ModelForm):
    class Meta:
        model = Gif
