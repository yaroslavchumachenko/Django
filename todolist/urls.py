from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("home/", views.home, name="home"),
    path("authorisation/", views.get_name,name = 'authorisation'),
    
    # HOMEWORK

    path("node/", views.nodes, name="homework")

    # HOMEWORK

]