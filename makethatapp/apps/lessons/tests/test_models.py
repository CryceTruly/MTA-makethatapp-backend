from makethatapp.apps.lessons.tests.test_base import LessonsTestBase


class ModelTest(LessonsTestBase):

    def test_str_representation(self):
        self.assertEquals(str(self.lesson), "hello")
