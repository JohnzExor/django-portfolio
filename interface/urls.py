from django.urls import path
from .views import Home, Contact, Projects

urlpatterns = [
    path("", Home.as_view()), 
    path("projects", Projects.as_view()),
    path("contact", Contact.as_view())
    ]
