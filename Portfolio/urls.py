from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("About/", views.about, name="about"),
    path("Projects/", views.project, name="project"),
    path("Contact/",views.contact, name="contact"),
    path('Contact/submit/', views.contact_submit, name='contact_submit'),
]