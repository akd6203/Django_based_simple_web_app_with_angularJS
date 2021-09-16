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

    def get_queryset(self):
        return Teacher.objects.prefetch_related(
            Prefetch(
                'my_students',
                queryset=Student.objects.only('id', 'name')
            )
        ).order_by('-created_on')

    def perform_create(self, serializer):
        if serializer.is_valid():
            req_data = self.request.data
            students_ids = req_data.pop('selected_student_ids')
            new_obj = serializer.save(**req_data)
            for student in Student.objects.filter(id__in=students_ids):
                new_obj.my_students.add(student)
            new_obj.save()
        return new_obj

    def perform_update(self, serializer):
        instance = self.get_object()
        if serializer.is_valid():
            req_data = self.request.data
            students_ids = req_data.pop('selected_student_ids')
            removed_students = req_data.pop('students_ids_removed')
            added_studnets = req_data.pop('students_ids_added')
            updated_obj = serializer.save(**req_data)
            for student in Student.objects.filter(id__in=removed_students):
                updated_obj.my_students.remove(student)
            for student in Student.objects.filter(id__in=added_studnets):
                updated_obj.my_students.add(student)
            updated_obj.save()
        return updated_obj



class StudentView(viewsets.ModelViewSet):
    """
    Teacher viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):
        return Student.objects.prefetch_related(
            Prefetch(
                'my_teachers',
                queryset=Teacher.objects.all().only('id', 'name')
            )
        ).order_by('-created_on')

    def perform_create(self, serializer):
        if serializer.is_valid():
            req_data = self.request.data
            taechers_ids = req_data.pop('selected_teacher_ids')
            new_obj = serializer.save(**req_data)
            for teacher in Teacher.objects.filter(id__in=taechers_ids):
                new_obj.my_teachers.add(teacher)
            new_obj.save()
        return new_obj

    def perform_update(self, serializer):
        instance = self.get_object()
        if serializer.is_valid():
            req_data = self.request.data
            teacher_ids = req_data.pop('selected_teacher_ids')
            removed_teacher = req_data.pop('teachers_ids_removed')
            added_teacher = req_data.pop('teachers_ids_added')
            updated_obj = serializer.save(**req_data)
            for teacher in Teacher.objects.filter(id__in=removed_teacher):
                updated_obj.my_teachers.remove(teacher)
            for teacher in Teacher.objects.filter(id__in=added_teacher):
                updated_obj.my_teachers.add(teacher)
            updated_obj.save()
        return updated_obj

    @action(detail=False, methods=['get'], url_path='star_students')
    def get_star_students(self, request):
        star_student_query = self.get_queryset()
        queryset = self.filter_queryset(star_student_query.filter(star_student=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
