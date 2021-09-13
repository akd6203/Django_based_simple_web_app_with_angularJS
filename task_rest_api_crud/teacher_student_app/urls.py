from django.conf.urls import url
from teacher_student_app.views import HomeTemplateViewSet

urlpatterns = [
    url(r'', HomeTemplateViewSet.as_view(), name='home'),
]
