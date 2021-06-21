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
    file = models.FileField(upload_to=file_upload_path, validators=[validate_file_extension],
                           null=False, blank=True,)

    def upload_file_url(self):
        last_id = Video.objects.aggregate(Max('id')).get('id__max', 0) or 0
        latest_id = last_id + 1
        return '//video//{0}'.format(latest_id)

class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255,blank=True)
    pred =  models.CharField(max_length=255,blank=True)
    n =  models.CharField(max_length=255,blank=True)

    image = ProcessedImageField(upload_to=file_upload_path,
                                processors=[ResizeToCover(1920, 1280)],
                                format='JPEG',
                                options={'quality': 100},
                                storage= FileSystemStorage(location=settings.MEDIA_ROOT)
                                )
    def image_url(self):
        if not self.image.url:
            return None
        return '{0}//{1}'.format(settings.CUSTOM_IMAGES_HOST_URL, self.image.url)

    def upload_file_url(self):
        last_id = Prediction.objects.aggregate(Max('id')).get('id__max', 0) or 0
        latest_id = last_id + 1
        return '//splitted//{0}'.format(latest_id)

#  class IntelligenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         #model = Intelligence
#         fields = ['id','n','pred','image']





