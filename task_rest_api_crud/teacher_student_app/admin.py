from django.contrib import admin
from .models import (
    Teacher, Student, TeacherFavStudent
)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TeacherFavStudent)
