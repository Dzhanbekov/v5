from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'




class About(TemplateView):
    template_name = 'about.html'