from django.urls import path
from . import views
from blogs import views as blog_views

urlpatterns = [
    # path("", views.rest_view),
    path("", blog_views.show_blogs),
    path("about/", views.show_about, name="about"),
    path("contact/", views.show_contact, name="contact"),
]