from django.conf.urls import url, include
from rest_framework import routers
from .views import TeacherView, StudentView

api_router = routers.DefaultRouter(trailing_slash=False)
api_router.register(r'teacher', TeacherView)
api_router.register(r'student', StudentView)

urlpatterns = [
    url(r'', include(api_router.urls))
]
