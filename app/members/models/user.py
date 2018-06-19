from django.db import models

__all__ = (
    'BlogUser',
)


class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    # 친구추가 기능 팔로우
    following = models.ManyToManyField(
        'self',
        related_name='my_friends',
        # symmetrical=False로 해주어야 인스타그램의 팔로우 개념처럼 가능
        # True로 하면 내가 추가하면 상대방도 추가가 되어버림
        symmetrical=False,
        blank=True,
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
