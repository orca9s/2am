from django.db import models

from members.models import BlogUser


class UserInfo(models.Model):
    name = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
