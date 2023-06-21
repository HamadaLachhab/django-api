from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class TaggedItemManager(models.Manager):
  def get_tags_for(self,obj_type,obj_id):
    
    contenttype= ContentType.objects.get_for_model(obj_type)# we get  content type  object 
    return TaggedItem.objects \
      .select_related('tag')  \
      .filter(
      content_type=contenttype,
      object_id=obj_id
    )

class Tag(models.Model):
  label = models.CharField(max_length=255)


class TaggedItem(models.Model):
  objects=TaggedItemManager()
  tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
  # product =models.ForeignKey(Product) we need to import 
   #Type and ID   generic 
  content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE) #respect name of the field 
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey()