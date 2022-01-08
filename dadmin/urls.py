from .views import DmallTokenObtainPairView, CaptchaAPIView
from django.urls import path


urlpatterns = [ 
    path('mytoken/', DmallTokenObtainPairView.as_view(), name='mytoken'),
    path('captcha/', CaptchaAPIView.as_view(), name='captcha_api'), 
]




