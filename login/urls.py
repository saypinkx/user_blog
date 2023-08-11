from django.urls import path
from . import views
urlpatterns = [
    path('', views.LoginView.as_view()),
    path('posts', views.PostView.as_view())
]