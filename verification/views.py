from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import CUSTOMEUSER
from rest_framework.permissions import IsAuthenticated




@api_view(['POST'])
def User_sign_up(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response(
            {
                "message":"All fields are required !"
            },status=400
        )
    
    if CUSTOMEUSER.objects.filter(email=email).exists():
        return Response(
            {
                "message":"User with this email already exists !"
            },status=400
        )
    
    user = CUSTOMEUSER.objects.create_user(username=username,email=email,password=password)
    user.save()

    return Response(
        {
            "message":"User created successfully !"
        },status=201
    )

