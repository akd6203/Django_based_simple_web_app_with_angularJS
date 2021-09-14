from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from teacher_student_app.models import Teacher, Student
from faker import Faker


class Command(BaseCommand):
    help = 'populate fake data for Teachers and student'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        """
        this is custom comand for populating data fake data dynamicaly
        """
        total = kwargs['total']
        random_subjects = ['Art', 'Business', 'studies', 'Citizenship', 'Critical',
                            'reading', 'Dance', 'Design', '&', 'technology', 'Drama',
                            'English', 'Geography', 'History', 'Information', 'and',
                            'communication', 'technology', 'Languages', 'Mathematics',
                            'Modern', 'studies', 'Music']
        fake = Faker()
        teacher_objs = [
            Teacher(
                name=fake.name(),
                age=fake.random_int(25, 60),
                fav_subject=fake.random_choices(random_subjects, 1),
            )
            for e in range(total)
        ]
        students_objs = [
            Student(
                name=fake.name(),
                age=fake.random_int(10, 25),
            )
            for e in range(total)
        ]
        bulk_teachers_objs = Teacher.objects.bulk_create(teacher_objs)
        self.stdout.write(self.style.SUCCESS('success - {} teachers fake objcet created successfully !!!.'.format(total)))
        bulk_students_objs = Student.objects.bulk_create(students_objs)
        self.stdout.write(self.style.SUCCESS('success - {} students fake objcet created successfully !!!.'.format(total)))
        all_students = list(Student.objects.all())
        all_teachers = list(Teacher.objects.all())
        # now create a relations
        import random
        for teacher in Teacher.objects.filter(my_students=None):
            for k in range(fake.random_int(1, 5)):
                teacher.my_students.add(random.choice(all_students))
            teacher.save()
        for student in Student.objects.filter(my_teachers=None):
            for k in range(fake.random_int(1, 5)):
                student.my_teachers.add(random.choice(all_teachers))
            student.save()
        self.stdout.write(self.style.SUCCESS('success - teachers and students data ready for testing !!!.'))
        self.stdout.write(self.style.SUCCESS('success - Command finished.'))
