from rest_framework import serializers
from teacher_student_app.models import Teacher, Student


class RealtedStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = ('id', 'name')


class RealtedTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'name')


class TeacherSerializer(serializers.ModelSerializer):
    my_students = serializers.SerializerMethodField()

    def get_my_students(self, obj):
        serializer = RealtedStudentSerializer(
            instance=obj.my_students.all(), many=True)
        return serializer.data


    class Meta:
        model = Teacher
        fields = ('id','name', 'age','my_students', 'fav_subject', 'created_on')


class StudentSerializer(serializers.ModelSerializer):
    my_teachers = serializers.SerializerMethodField()

    def get_my_teachers(self, obj):
        serializer = RealtedTeacherSerializer(
            instance=obj.my_teachers.all(), many=True)
        return serializer.data

    class Meta:
        model = Student
        fields = ('id', 'name','age', 'my_teachers','star_student', 'created_on')
