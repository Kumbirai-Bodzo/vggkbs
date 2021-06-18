import os

import cv2
import pandas as pd
from django.conf import settings
from django.core.files.base import ContentFile, File
from django.core.files.storage import FileSystemStorage, default_storage
from django.dispatch import receiver
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from tensorflow.keras.preprocessing import image

from Intelligence.predictions import VggProcess
from Intelligence.utils import create_directory


# Create your views here.
class IntelligenceView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]  # IsAuthenticated
    parser_class = (FileUploadParser,)

    # variables
    path = settings.MEDIA_ROOT+ "\\"
    srcVideoUrl = settings.MEDIA_ROOT+ "\\uploaded\\uploaded_video.mp4"
    splitedImagesUrl = settings.MEDIA_ROOT+ "\\splited\\"

    def post(self, request):

        
        create_directory(self.path+ 'videos')
        create_directory(self.path+ 'splited')
 
        file  = request.FILES['video']
    
        vprocess = VggProcess()
        vprocess.uploadVideo(file)
        

        # splitting video into images
        vprocess.split_images_from_video(self.splitedImagesUrl,self.srcVideoUrl)
        #ret = vprocess.iterate_prediction(self.splitedImagesUrl,)

        return Response(dict(), status=200)

    def get(self, request):

        #print(path)
        #img_list = os.listdir(path)
        #context = {"images": img_list}
        # details =dict()
        # arr = {'one':'two','three':'three'}

        # details = dict(details, **arr)
        # details = dict(details, **{'name':'https://'})
        vprocess = VggProcess()
        ret = vprocess.iterate_prediction(self.splitedImagesUrl,)
      
        return Response(ret, status =status.HTTP_200_OK)

        


        imageList = [
            {
        'n':'n1233',
        'name':'cat',
        'pred':'98',
        'image_url': 'http://localhost:8000/static/splited/0.jpg'
        
        },
        {
        'n':'n1233',
        'name':'cat',
        'pred':'98',
        'image_url': 'http://localhost:8000/static/splited/1.jpg'
        
        }]
    
        return Response(ret, status =status.HTTP_200_OK)

