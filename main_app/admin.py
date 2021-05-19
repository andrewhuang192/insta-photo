from django.contrib import admin
from .models import Photo, Comment, Tag

# Register your models here.
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Tag)
