from django.db import models

from members.models import BlogUser


class UserInfo(models.Model):
    name = models.OneToOneField(
        # OneToOne필드로 BlogUser와 연결 해주기
        BlogUser,
        # BlogUser가 있어야 UserInfo도 있을 수 있다.
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
