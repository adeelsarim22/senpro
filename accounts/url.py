from django.urls import path
from rest_framework_simplejwt import views as jwt

urlpatterns = [
    path('login/', jwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt.TokenRefreshView.as_view(), name='token_refresh'),
]
