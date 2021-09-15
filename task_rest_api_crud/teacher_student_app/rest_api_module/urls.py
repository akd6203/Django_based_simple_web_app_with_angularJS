from django.conf.urls import url, include
from rest_framework import routers
from .views import TeacherView, StudentView

api_router = routers.DefaultRouter(trailing_slash=False)
api_router.register(r'teacher', TeacherView)
api_router.register(r'student', StudentView)

# import ipdb; ipdb.set_trace()
urlpatterns = [
    url(r'', include(api_router.urls))
]

# urlpatterns = [
#     url(r'teachers/', TeacherView.as_view(), name='teachers_api'),
#     url(r'students/', TeacherView.as_view(), name='students_api')
#
# ]
