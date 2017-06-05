from django.db import models
from django.contrib.auth.models import User
from draceditor.models import DraceditorField
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

# Create your models here.

class Post(models.model):
    post_img = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)

