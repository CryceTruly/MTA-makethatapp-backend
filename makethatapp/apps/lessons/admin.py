from django.contrib import admin
from makethatapp.apps.lessons.models import Lesson
from django.utils.text import slugify


class LessonAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created_at')
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'body',)
    list_per_page = 25
    filter_horizontal = ()
    view_on_site = False

    def save_model(self, request, obj, form, change):
        last_lesson = Lesson.objects.latest('id')
        if "add" in request.path:
            obj.slug = slugify(obj.title+" "+str(last_lesson.id+1))
        return super().save_model(request, obj, form, change)


admin.site.register(Lesson, LessonAdmin)
