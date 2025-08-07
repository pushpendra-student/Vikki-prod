from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    
class TaggedItem(models.Model):
    # what tag applied to what object 
    # if we delete the tag we want to delete all associated ibject
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    # Type (product , video , artical)
    # ID
    
    # get the object type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # get the object id
    object_id = models.PositiveIntegerField()
    # to get actual product object
    content_object = GenericForeignKey()