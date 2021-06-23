from cloudinary.models import CloudinaryField
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.aggregates import Max
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToCover
from rest_framework import serializers

from Intelligence.utils import file_upload_path
from Intelligence.validators import validate_file_extension


# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key =True)


    file =  CloudinaryField(folder = "videos/",public_id = "uploaded_video",overwrite = True, resource_type = "video")

    def upload_file_url(self):
        last_id = Video.objects.aggregate(Max('id')).get('id__max', 0) or 0
        latest_id = last_id + 1
        return '{0}'.format(latest_id)

    def __str__(self):
        return '{0}'.format(self.id)

class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255,blank=True)
    pred =  models.CharField(max_length=255,blank=True)
    n =  models.CharField(max_length=255,blank=True)
    file = models.FileField(upload_to='images/',blank=True)
    # image =  CloudinaryField(folder = "splitted/",public_id = "1",overwrite = True, resource_type = "image")



    def file_url(self):
        if not self.file:
            return None
        return self.file.url

    def upload_file_url(self):
        last_id = Prediction.objects.aggregate(Max('id')).get('id__max', 0) or 0
        latest_id = last_id + 1
        return '//splitted//{0}'.format(latest_id)





