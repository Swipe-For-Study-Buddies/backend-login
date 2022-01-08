from django.utils import timezone 
from rest_framework import serializers 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from django.contrib.auth import authenticate 
from utils.get_token import get_tokens_for_user 
from captcha.fields import CaptchaStore 


class DmallTokenObtainPairSerializer(TokenObtainPairSerializer): 
    captcha = serializers.CharField(
        max_length=4, 
        required=True, 
        trim_whitespace=True, 
        min_length=4, 
        error_messages={ 
            "max_length": "圖片驗證碼僅允許4位", 
            "min_length": "圖片驗證碼僅允許4位", 
            "required": "請輸入圖片驗證碼" 
        }, 
        help_text="圖片驗證碼") 
    imgcode_id = serializers.CharField(required=True, write_only=True, help_text="圖片驗證碼id") 
    
    @classmethod 
    def get_token(cls, user): 
        token = super().get_token(user) 
        token['captcha'] = user.captcha 
        token['imgcode_id'] = user.imgcode_id 
        return token 
    def validate_captcha(self, captcha): # 驗證碼驗證 
        try: 
            captcha = captcha.lower() 
        except: 
            raise serializers.ValidationError("驗證碼錯誤") 
        img_code = CaptchaStore.objects.filter( 
            id = int(self.initial_data['imgcode_id'])
        ).first()                                              
        if img_code and timezone.now() > img_code.expiration: 
            raise serializers.ValidationError("圖片驗證碼過期") 
        else: 
            if img_code and img_code.response == captcha: 
                pass 
            else: 
                raise serializers.ValidationError("驗證碼錯誤") 
        def validate(self, attrs): # 刪除驗證碼 
            del attrs['captcha'] 
            del attrs['imgcode_id'] 
            authenticate_kwargs = { 
                'username': attrs['username'],
                'password': attrs['password'], 
            } # 驗證當前登錄用戶 
            self.user = authenticate(**authenticate_kwargs) 
            if self.user is None: 
                raise serializers.ValidationError('帳號或密碼不正確') # 登錄成功返回token信息 
            token = get_tokens_for_user(self.user) 
            return token

