from django.test import TestCase
from makethatapp.apps.lessons.models import Lesson


class LessonsTestBase(TestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(title="hello", slug="", body="")
        return super().setUp()
