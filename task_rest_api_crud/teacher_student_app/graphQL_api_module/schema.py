import graphene
from graphene_django import DjangoObjectType
from django.db.models import Prefetch

from teacher_student_app.models import Teacher, Student

class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = ("id", "name", "age",  "fav_subject", "created_on", "my_students")


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "age", "star_student", "created_on", "my_teachers")


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    all_teachers = graphene.List(TeacherType)

    def resolve_all_students(root, info):

        return Student.objects.all()
        return Student.objects.prefetch_related(
            Prefetch(
                'my_teachers',
                queryset=Teacher.objects.only('id', 'name')
            )
        ).order_by('-created_on')

    def resolve_all_teachers(root, info):
        return Teacher.objects.all()

        return Teacher.objects.prefetch_related(
            Prefetch(
                'my_students',
                queryset=Student.objects.only('id', 'name')
            )
        ).order_by('-created_on')



schema = graphene.Schema(query=Query)
