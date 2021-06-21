import glob
import os

import cv2
import numpy as np
import pandas as pd
from django.conf import settings
from django.core.files.base import ContentFile, File
from django.core.files.storage import FileSystemStorage, default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.dispatch import receiver
from django.shortcuts import render
from django.template.loader import render_to_string
from keras.applications.vgg16 import VGG16
from rest_framework import status
from tensorflow.keras.applications.vgg16 import (decode_predictions,
                                                 preprocess_input)
from tensorflow.keras.preprocessing import image

from Intelligence.models import Prediction
from Intelligence.serializers.intelligence_serializer import \
    PredictionSerializer


class VggProcess():

    def iterate_prediction(self, splittedImagesUrl):

        image_list = []
        for filename in glob.glob('{}*jpg'.format(splittedImagesUrl))[:]: #assuming jpg
            details = dict()
            img = image.load_img(filename,color_mode='rgb', target_size=(224, 224))
            arr = self.convert_tonumpy(img)
            values = self.predict_images(arr)
            # values2= {'n':'n1233',
            # 'name':'cat',
            #     'pred':'98',}
            
            host_path = '{}/static/splited/{}'.format(settings.CUSTOM_IMAGES_HOST_URL, os.path.basename(filename)) 

            details = dict(details, **values)

            details = dict(details, **{'image_url':host_path})
    
            image_list.append(details)
            
        return image_list

    def saveimage(self, details):
        file_serializer = PredictionSerializer(data = details)
        if file_serializer.is_valid():
            file_serializer.save()
        
        print(file_serializer.errors)

   
    def convert_tonumpy(self, image_input):
        # Converts a PIL Image to 3D Numy Array
        x = image.img_to_array(image_input)
        x.shape
        # Adding the fouth dimension, for number of images
        x = np.expand_dims(x, axis=0)
        return x
    
    def predict_images(self, nparr):
        vgg16_weights = settings.MEDIA_ROOT+ "\\model\\vgg16_weights_tf_dim_ordering_tf_kernels.h5"
        #vgg16_weights = 'models/vgg16_weights_tf_dim_ordering_tf_kernels.h5'

        # model = VGG16(weights='imagenet')
        model = None

        try: 
            model = VGG16(weights = vgg16_weights)

        except Exception as e:
            model = VGG16(weights='imagenet')
            

        print(model)
        x = preprocess_input(nparr)
        features = model.predict(x)
        p = decode_predictions(features)
        dict = {
        'n':p[0][0][0],
        'name':p[0][0][1],
        'pred':p[0][0][2]}
        print(dict)

        return dict

    def split_images_from_video(self,request, splitedImagesUrl, srcVideoUrl):
        print('_______________________')
        vidcap = cv2.VideoCapture(srcVideoUrl)
        print(vidcap)

        print('reading images from video')
        currentframe = 0
        while(True):
            #print('read..')
            
            # reading from frame
            ret,frame = vidcap.read()
        
            if ret:
                # if video is still left continue creating images
                name = splitedImagesUrl + str(currentframe) + '.jpg'
                #print ('Creating...' + name)
                

                # mg = image.load_img(frame,color_mode='rgb', target_size=(224, 224))
                #ret,jpeg = cv2.imencode('.jpg', frame)
                #print(jpeg.tobytes())
                # import io
                # 
                # image = Image.open(io.BytesIO(jpeg.tobytes()))
                # import PIL.Image as Image
                # from django.core.files.uploadedfile import InMemoryUploadedFile

                # img_pill = Image.fromarray(frame, 'RGB')
          
                # img = InMemoryUploadedFile(img_pill, None, 'foo.jpg', 'image/jpeg', img_pill.tell, None)
                # request.FILES['image'] = img
                from cloudinary import CloudinaryImage

                # c = CloudinaryImage(img)
                #print(c)
                #cv2.imwrite(name, frame)
                ret, buf = cv2.imencode('.jpg', frame) # cropped_image: cv2 / np array
                content = ContentFile(buf.tobytes())
                p =  Prediction()
                p.file.save('{}.jpg'.format(currentframe), content)
                print(content)


                print(name)
                currentframe += 1
                # break
            

                # data = {
                #     'image': content , #CloudinaryImage(name).image(secure=True),
                #      'name': 'name',
                # 'pred': '0',
                # 'n':'0'
                # }
                 

                # file_serializer = PredictionSerializer(data =data)
                # if file_serializer.is_valid():
                #     file_serializer.save()
                #     break

                #     if os.path.exists(name):
                #         #os.remove(name)
                #         #break
                #         pass
                    

                    #return Response(file_serializer.data, status=status.HTTP_201_CREATED)
                # print(file_serializer.errors)
            
        
                # writing the extracted images
                # 
        
                # print(r)
        
                # increasing counter so that it will
                # show how many frames are created
                
            else:
                print('nothing to read now.')
                break
        
        vidcap.release()
        cv2.destroyAllWindows()
        print('finished reading images from video')
        print('_______________________')

    def uploadVideo(self, file):
        def delete_existing():
                full_path = os.path.join(settings.MEDIA_ROOT, 'uploaded/uploaded_video.mp4')
                 
                if os.path.exists(full_path):
                    os.remove(full_path)
                    return full_path
        delete_existing()
        fs = FileSystemStorage()
        fs.save('uploaded/uploaded_video.mp4', file)
        # uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        return 'video saved'


