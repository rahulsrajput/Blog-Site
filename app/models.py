from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='thumbnail', blank=True, null=True)
    author = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field()
    