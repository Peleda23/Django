from django.views.generic import TemplateView


# adding view for home page
class HomePageView(TemplateView):
    template_name = "home.html"
