from .test_base import LessonsTestBase
from django.contrib.admin.sites import AdminSite
from makethatapp.apps.lessons.admin import LessonAdmin
from makethatapp.apps.lessons.models import Lesson


class MockRequest(object):
    def __init__(self, user=None, path='/add'):
        self.user = user
        self.path = path


class CreateLessonForm(object):
    pass


class TestAdmin(LessonsTestBase):
    def test_save_model(self):
        self.admin = LessonAdmin(model=Lesson, admin_site=AdminSite)
        self.assertEqual(self.admin.save_model(MockRequest(), self.lesson, CreateLessonForm, True), None)