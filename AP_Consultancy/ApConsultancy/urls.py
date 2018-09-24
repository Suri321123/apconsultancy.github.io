from django.conf.urls import url
from ApConsultancy import views


urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'contact', views.contacts, name='contact'),
]