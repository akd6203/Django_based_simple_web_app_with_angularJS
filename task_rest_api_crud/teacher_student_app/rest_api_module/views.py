# rest_framework imports for api views and response
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from django.db.models import Prefetch

from .serializers import TeacherSerializer, StudentSerializer
from teacher_student_app.models import Teacher, Student


class TeacherView(viewsets.ModelViewSet):
    """
    Teacher viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    # def get_queryset(self):
    #     return Teacher.objects.prefetch_related(
    #         Prefetch(
    #             'my_students',
    #             queryset=Student.objects.only('id', 'name')
    #         )
    #     )



class StudentView(viewsets.ModelViewSet):
    """
    Teacher viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    # def get_queryset(self):
    #     return Teacher.objects.prefetch_related(
    #         Prefetch(
    #             'my_students',
    #             queryset=Student.objects.all().only('id', 'name')
    #         )
    #     )
