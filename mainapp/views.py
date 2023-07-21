from datetime import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView

from mainapp import models as mainapp_models


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


class NewsPageView(TemplateView):
    NEWS_QTY = 5

    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["news_qs"] = mainapp_models.News.objects.all()[:5]

        return context
