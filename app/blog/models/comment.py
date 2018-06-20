from django.db import models

from blog.models import Post
from members.models import BlogUser


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comments_likes'
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='user_comments_likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
