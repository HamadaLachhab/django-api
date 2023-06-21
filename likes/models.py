from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



# Create your models here.
class LikedItem(models.Model):
  user =models.ForeignKey(User,on_delete=models.CASCADE) #if a user is delted all the like will be deleted
  content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
  object_id=models.PositiveIntegerField()
  content_object=GenericForeignKey()