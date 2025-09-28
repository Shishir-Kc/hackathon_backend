from django.urls import path
from .views import Home,upload_user_image

urlpatterns = [

    path('dashboard/',Home),
    path('upload/image/',upload_user_image),
    

]