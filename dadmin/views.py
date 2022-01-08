from django.shortcuts import render
import base64
import json
from django.http import HttpResponse 
from rest_framework.views import APIView 
from captcha.views import CaptchaStore, captcha_image

from rest_framework import serializers 
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializer import DmallTokenObtainPairSerializer 

from utils.hash import get_hash
from .models import Users


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

class RegisterAPIView(APIView):
    def post(self, request):  
        json_data = json.loads(request.body)    
        _email = json_data["email"]
        _password = json_data["password"]
        print(_email, _password)
        hash_password, salt= get_hash(_password)
        if Users.objects.filter(email = _email).exists():
            fail_json = json.dumps({"message": "AccountAlreadyExist"})
            return HttpResponse(fail_json, content_type="application/json", status= 400)  
        Users.objects.create(email=_email, password=hash_password, salt=salt)            
        success_json = json.dumps({"message": "OK"})
        return HttpResponse(success_json, content_type="application/json")




# Create your views here.
