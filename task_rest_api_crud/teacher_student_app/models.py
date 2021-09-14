from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    fav_subject = models.CharField(max_length=32)
    my_students = models.ManyToManyField("Student", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Teacher name is: {}".format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    my_teachers =  models.ManyToManyField("Teacher", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Student name is: {}".format(self.name)


class TeacherFavStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} is fav student of {} teacher:".format(
                                                self.Student.name,
                                                self.teacher.name)
