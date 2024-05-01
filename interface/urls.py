from django.urls import path
from .views import Home, Contact, Projects, About

urlpatterns = [
    path("", Home.as_view()), 
    path("about", About.as_view()),
    path("projects", Projects.as_view()),
    path("contact", Contact.as_view())
    ]
