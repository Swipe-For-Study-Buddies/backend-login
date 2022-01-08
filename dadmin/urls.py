from .views import DmallTokenObtainPairView, CaptchaAPIView, RegisterAPIView
from django.urls import path


urlpatterns = [ 
    path('mytoken/', DmallTokenObtainPairView.as_view(), name='mytoken'),
    path('captcha/', CaptchaAPIView.as_view(), name='captcha_api'), 
    path('register', RegisterAPIView.as_view(), name='registerAPI')
]




