from django.db import models

from members.models import BlogUser


class Post(models.Model):
    # 다대일 관계이기 때문에 Foreignkey?
    # BlogUser에서 받아오기 때문에 변수명은 user로 해주는게 좀 더 맞다
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_post',
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    # 여기선 post에서 받아오기 때문에 변수명을 post로 지정
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_likes',
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='user_post_likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
