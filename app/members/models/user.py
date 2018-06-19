from django.db import models


class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        related_name='my_friends',
        symmetrical=False,
        blank=True,
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
        blank=True,
    )