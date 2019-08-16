from django.db import models
from ckeditor.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField


class Lesson(models.Model):
    title = models.CharField(max_length=500)
    body = RichTextUploadingField()  
    tagsList = ArrayField(ArrayField(
        models.CharField(max_length=10, blank=True, null=True), size=8,
        default=list
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
