from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse
# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=50,default="Get Rick Rolled")
    url = EmbedVideoField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("data:detail", kwargs={"pk": self.pk})
