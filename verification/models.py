from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 

class CUSTOMEUSER(AbstractUser):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4,editable=False)
    user_image = models.URLField(max_length=500)


    def __str__(self):
        return self.username

