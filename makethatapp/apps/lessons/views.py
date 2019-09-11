from rest_framework import viewsets
from .models import Lesson
from .serializers import LessonSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Lesson.objects.all()

    serializer_class = LessonSerializer
