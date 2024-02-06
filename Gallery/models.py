import os
import random
from time import time
from django.db.models.fields.related import ForeignKey
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Anchor
from PIL import Image
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def photo_path_post(instance, filename):
    current_dateTime = datetime.now()
    basefilename, file_extension = os.path.splitext(filename)
    # chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    # randomstr= ''.join((random.choice(chars)) for x in range(10))
    return 'images/{basename}{username}-{randomstring}{ext}'.format(username=instance.user.username, basename="img-", randomstring=current_dateTime, ext=file_extension)

class Images(models.Model):
    current_date = datetime.now().strftime ("%Y-%m-%d")
    user = ForeignKey(User, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=photo_path_post, help_text="Post",
                                     verbose_name="Post",
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',
                                     options={'quality': 80})
    description = models.TextField( blank=True)
    title = models.CharField(max_length=100, blank=True)
    uploaded_on = models.DateField(default=timezone.now())
    

    def __str__(self):
        return (self.caption + "-" + self.user.username)
    def get_absolute_url(self):
        return reverse('gallery')