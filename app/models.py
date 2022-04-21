from django.db import models


def upload_image_author(instance, filename):
    return f"{instance.id}-{filename}"


class Author(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(verbose_name="picture", upload_to=upload_image_author, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Articles(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='category_author')
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='article_author')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=5000)

