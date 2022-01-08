from rest_framework_simplejwt.tokens import RefreshToken 


def get_tokens_for_user(user): # 手動返回令牌 
    refresh = RefreshToken.for_user(user) 
    return { 
        'refresh': str(refresh), 
        'access': str(refresh.access_token), 
    }

