from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,    TokenRefreshView
from .views import User_sign_up
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',User_sign_up,name='signup')
]
