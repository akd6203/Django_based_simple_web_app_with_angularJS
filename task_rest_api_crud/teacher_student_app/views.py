from django.views.generic import TemplateView


class HomeTemplateViewSet(TemplateView):
    template_name = "index.html"
