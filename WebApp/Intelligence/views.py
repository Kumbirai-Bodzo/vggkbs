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

from Intelligence.models import Prediction, Video
from Intelligence.predictions import VggProcess
from Intelligence.serializers.intelligence_serializer import \
    PredictionSerializer
from Intelligence.serializers.video_serializer import VideoSerializer


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
        # file  = request.FILES['video']
        data = request.data
        file_serializer = VideoSerializer(data=data)


        
        if file_serializer.is_valid():
            file_serializer.save()
            Prediction.objects.all().delete()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        print(file_serializer.errors)
        return Response({'message':'failed uploading video'}, status =status.HTTP_417_EXPECTATION_FAILED)




        # return Response(dict(), status=200)

    def get(self, request):
        # create_directory(self.path+ 'splited')
        #Prediction.objects.all().delete()

        vprocess = VggProcess()
        p = Prediction.objects.all()
        ret = vprocess.iterate_prediction(p,self.splitedImagesUrl,)
     
        #video = Video.objects.last()
        #print(video.file.url)
        #vprocess.split_images_from_video(request, self.splitedImagesUrl,video.file.url)

        ser = PredictionSerializer(p , many=True)

        print(ser.data)

      
        return Response(ser.data, status =status.HTTP_200_OK)

class PredictView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]  # IsAuthenticated

    # variables
    # path = settings.MEDIA_ROOT+ "\\"
    # srcVideoUrl = settings.MEDIA_ROOT+ "\\uploaded\\uploaded_video.mp4"
    splitedImagesUrl = settings.MEDIA_ROOT+ "\\splited\\"

 
    def get(self, request):

        vprocess = VggProcess()
        p = Prediction.objects.all()
        try:
            vprocess.iterate_prediction(p,self.splitedImagesUrl,)
            return Response({'message':'successfully finished prediction'}, status =status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message':'failed predicting'}, status =status.HTTP_417_EXPECTATION_FAILED)
     
        #ser = PredictionSerializer(p , many=True)
        #print(ser.data)
        

class PredictedListView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]  # IsAuthenticated

 
    def get(self, request):

        p = Prediction.objects.exclude(n__isnull=True).exclude(pred__exact='')
  
        if p.exists():
            ser = PredictionSerializer(p , many=True)
            return Response(ser.data, status =status.HTTP_200_OK)
        return Response({'message':'list empty'}, status =status.HTTP_417_EXPECTATION_FAILED)


      
        

        # print(ser.data)


      
        



class SplitImagesFromVideo(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]  # IsAuthenticated
    splitedImagesUrl = settings.MEDIA_ROOT+ "\\splited\\"

 
    def get(self, request):
        video = Video.objects.last()

        vprocess = VggProcess()

        try:
            vprocess.split_images_from_video(request, self.splitedImagesUrl, video.file.url)
            return Response({'message':'finished spliting video'}, status =status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'message':'failed spliting video'}, status =status.HTTP_417_EXPECTATION_FAILED)


        # print(ser.data)

      
        
