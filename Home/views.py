from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import CUSTOMEUSER
from rest_framework.permissions import IsAuthenticated
from .models import Hotel,Places
from .tools import upload_to_bucket
from rest_framework import status

@api_view(['GET'])
def Home(request):
    data = []

    user = request.user
    places = Places.objects.all()
    for place in places:
        data.append(
            {
                "place_name":place.place_name,
                "description":place.description,
                "is_user_went":place.is_user_went,
                "went_at":place.went_at,
                "place_images":[image.images_url for image in place.place_images.all()],
                "region":place.region,
                "type":place.type,
                "difficulty_level":place.difficulty_level,

            }
        )
    return Response(data)


@api_view(['POST'])
def upload_user_image(request):
    image = request.FILES['file']
    if not image:
        return Response (
            {
                "message":"empty image field ! "
            }, status=status.HTTP_204_NO_CONTENT

        )    
    response = upload_to_bucket(bucket_name="USER_IMAGES",file_name=image.name,file_bytes=image.read())
    
    print(response)






