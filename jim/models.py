from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    """記事(タイトルorテーマのみ)"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # タイトル
    title = models.CharField(
        max_length=32,
        null=False,
        blank=False
    )

    def __str__(self):
        return "%s" % self.title


class Point(models.Model):
    """記事の要点"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # 記事
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    # 内容
    content = models.CharField(
        max_length=64,
        null=False,
        blank=False
    )

    def __str__(self):
        return "%s" % self.content


class Thought(models.Model):
    """思考"""

    # ユーザー
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # 記事
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    # 要点
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE
    )

    # 思考のタイプ
    # 0 .. なぜなら~ ( 理由 )
    # 1 .. そうはいっても~ ( 反論、ツッコミ )
    REASONING = 0
    OBJECTION = 1
    THOUGHT_TYPES = (
        (REASONING, "なぜなら~"),
        (OBJECTION, "そうはいっても~"),
    )
    thought_type = models.IntegerField(
        choices=THOUGHT_TYPES
    )

    # 思考の内容
    content = models.CharField(
        max_length=64,
        null=False,
        blank=False
    )

    def __str__(self):
        return "%s" % self.content