from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.show_blogs, name="blogs"),
    path("<int:blog_id>/", views.detail, name="detail")
]
