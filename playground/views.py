from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import *
from tags.models import TaggedItem
from  django.db.models import Q,F,Value
from  django.db.models.functions import Concat
from django.db import transaction


def say_hello(request):    
    return render(request,'hello.html')
    