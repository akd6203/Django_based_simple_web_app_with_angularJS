from django.views.generic import TemplateView
from .models import Student, Teacher
import json

class HomeTemplateViewSet(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateViewSet, self).get_context_data(**kwargs)
        context['students_names'] = json.dumps(list(Student.objects.values('id', 'name')))
        context['teachers_names'] = json.dumps(list(Teacher.objects.values('id', 'name')))
        return context
