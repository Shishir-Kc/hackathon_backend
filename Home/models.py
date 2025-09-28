from django.db import models
import uuid 
from verification.models import CUSTOMEUSER

class Places_images(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    images_url = models.URLField(max_length=500)
    image_name = models.CharField(max_length=100,verbose_name="Image Name",null=True,blank=True)
    class Meta:
        verbose_name_plural = "Places_images"
        verbose_name = "Places_image"

    def __str__(self):
        return str(self.image_name)
   
    
class Highlights(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    highlight = models.CharField(max_length=200,verbose_name="Highlight")

    def __str__(self):
        return self.place.place_name + " - " + self.highlight
    

class Places(models.Model):
    class DIFFICULTY_LEVEL(models.TextChoices):
        EASY = 'Easy'
        MEDIUM = 'Medium'
        HARD = 'Hard'

    class REGION(models.TextChoices):
        AANAPURNA = 'Aanapurna'
        CENTRAL_NEPAL = 'Central Nepal'
        EASTERN_NEPAL = 'Eastern Nepal'
        WESTERN_NEPAL = 'Western Nepal'
        FAR_WESTERN_NEPAL = 'Far Western Nepal'
        MANASLU = 'Manaslu'

    class TYPE(models.TextChoices):
        VILLAGE = 'Village'
        TOWN = 'Town'
        LAKE = 'Lake'
        PLANTATION = 'Plantation' 
        TREK = 'Trek'
        NATURE  = 'Nature'


    user = models.ForeignKey(CUSTOMEUSER,on_delete=models.CASCADE,null=True,blank=True)
    place_name = models.CharField(max_length=100,verbose_name="Place Name")
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    place_images = models.ManyToManyField(Places_images,blank=True)
    is_user_went = models.BooleanField(default=False)
    went_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=10,choices=DIFFICULTY_LEVEL.choices,default=DIFFICULTY_LEVEL.EASY)
    region = models.CharField(max_length=20,choices=REGION.choices,default="Null")
    type = models.CharField(max_length=20,choices=TYPE.choices,default="Null")
    highlights = models.ManyToManyField(Highlights,blank=True)
    rating = models.FloatField(default=0.0)


    def __str__(self):
        return self.place_name

class Vehicles(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    vehicle_name = models.CharField(max_length=100,verbose_name="Vehicle Name")
    vehicle_number = models.CharField(max_length=100,verbose_name="Vehicle Number")
    user = models.ForeignKey(CUSTOMEUSER,on_delete=models.CASCADE)


class Hotel_Images(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image_url = models.URLField(max_length=500)

    class Meta:
        verbose_name_plural = "Hotel_Images"
        verbose_name = "Hotel_Image"

    def __str__(self):
        return self.hotel.hotel_name
    


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    hotel_name = models.CharField(max_length=100,verbose_name="Hotel Name")
    user = models.ForeignKey(CUSTOMEUSER,on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    hotel_images = models.ManyToManyField(Hotel_Images,blank=True)




class Vehicles_images(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)

    class Meta:
        verbose_name_plural = "Vehicles_images"
        verbose_name = "Vehicles_image"

    def __str__(self):
        return self.id
    



class Booking_Trip(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(CUSTOMEUSER,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    place = models.ForeignKey(Places,on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField()
    booking_date = models.DateField()


    def __str__(self):
        return str(self.user.username) + " - " + str(self.place.place_name)
    

