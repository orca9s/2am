from django.db import models

from members.models import BlogUser


class Post(models.Model):
    # 다대일 관계이기 때문에 Foreignkey?
    # BlogUser에서 받아오기 때문에 변수명은 user로 해주는게 좀 더 맞다
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='user_post',
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def like_users(self):
        return [post_like.user for post_like in PostLike.objects.filter(post=self)]
        # return f'이 글에 좋아요를 누른 사람{self.post_likes.all()}'

    def __str__(self):
        return f'제목:{self.title}'


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

    def __str__(self):
        return f'{self.user}'
