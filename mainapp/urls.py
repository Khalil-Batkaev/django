from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('hello/', views.hello),
    path('', views.MainPageView.as_view(), name="main_page"),
    path('contacts/', views.ContactsPageView.as_view(), name="contacts"),
    path('courses_list/', views.CoursesPageView.as_view(), name="courses"),
    path('doc_site/', views.DocPageView.as_view(), name="doc_site"),
    path('news/', views.NewsPageView.as_view(), name="news"),
]
