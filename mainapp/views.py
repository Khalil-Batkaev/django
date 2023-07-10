from django.http import HttpResponse
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse('hello!')


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocPageView(TemplateView):
    template_name = 'mainapp/do_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'
