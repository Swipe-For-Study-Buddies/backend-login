from django.shortcuts import render
import base64
import json
from django.http import HttpResponse 
from rest_framework.views import APIView 
from captcha.views import CaptchaStore, captcha_image

from rest_framework import serializers 
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializer import DmallTokenObtainPairSerializer 


class DmallTokenObtainPairView(TokenObtainPairView): # 登錄成功返回token 
    serializer_class = DmallTokenObtainPairSerializer

class CaptchaAPIView(APIView): 
    def get(self, request): 
        hashkey = CaptchaStore.generate_key() 
        try:
            #獲取圖片id 
            id_ = CaptchaStore.objects.filter(hashkey=hashkey).first().id 
            imgage = captcha_image(request, hashkey) #將圖片轉換為base64 
            image_base = 'data:image/png;base64,%s' % base64.b64encode(imgage.content).decode('utf-8') 
            json_data = json.dumps({"id": id_, "image_base": image_base }) # 批量刪除過期驗證碼 
            CaptchaStore.remove_expired() 
        except: json_data = None 
        return HttpResponse(json_data, content_type="application/json")





# Create your views here.
