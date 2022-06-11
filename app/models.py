from django.db import models
from uuid import uuid4

from rest_framework.exceptions import ValidationError

from rest_framework import serializers


def upload_image_author(instance, filename):
    return f"{instance.id}-{filename}"


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    picture = models.ImageField(verbose_name="picture", upload_to=upload_image_author, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='article_author')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=10000)
    first_paragraph = models.CharField(max_length=200)
    body = models.TextField()

    def clean(self):
        if self.body is not None:
            if len(self.body) < 50:
                raise serializers.ValidationError({"body": 'body minimum digits is 50'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

