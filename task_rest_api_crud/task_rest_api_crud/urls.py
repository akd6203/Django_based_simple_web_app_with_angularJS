"""task_rest_api_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from teacher_student_app.graphQL_api_module.schema import schema

urlpatterns = [
    url('admin/', admin.site.urls, name='admin'),
    url(r'app/', include(('teacher_student_app.urls', 'teacher_student_app'),
                                    namespace='core_app')),
    url(r'api/', include(('teacher_student_app.rest_api_module.urls', 'teacher_student_API'),
                                    namespace='rest_api')),
    url(r"graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
