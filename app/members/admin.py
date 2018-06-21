from django.contrib import admin

from .models import BlogUser, UserInfo

admin.site.register(BlogUser)
admin.site.register(UserInfo)
