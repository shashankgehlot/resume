from django.urls import path
from . import views
from .views import GeeksListView

urlpatterns = [
    path('<slug:slug>/',GeeksListView.as_view(),name='blog_home'),
]