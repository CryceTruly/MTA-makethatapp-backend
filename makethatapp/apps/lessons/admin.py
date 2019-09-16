from django.contrib import admin
from makethatapp.apps.lessons.models import Lesson
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite


class LessonAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created_at')
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'body',)
    list_per_page = 25
    filter_horizontal = ()
    view_on_site = False

    def save_model(self, request, obj, form, change):
        last_lesson = Lesson.objects.latest('id')

        if last_lesson:
            if "add" in request.path:

                try:
                    obj.slug = slugify(obj.title+" "+str(last_lesson.id+1))
                except Exception as identifier:
                    obj.slug = slugify(obj.title)
                    
        return super().save_model(request, obj, form, change)


AdminSite.index_title = ugettext_lazy('BACKEND ADMINSTRATION')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Lesson, LessonAdmin)
