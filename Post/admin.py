from django.contrib import admin
from .models import init_img, post, comment, Key

# Register your models here.

admin.site.register(init_img)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(Key)