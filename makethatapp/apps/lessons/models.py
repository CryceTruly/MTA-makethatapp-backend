from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.postgres.fields import ArrayField


class Lesson(models.Model):
    title = models.TextField()
    body = RichTextUploadingField()
    tagsList = ArrayField(ArrayField(
        models.CharField(max_length=100, blank=True, null=True), size=100,
        default=list
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    thumbnail=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
