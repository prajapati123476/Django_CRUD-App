from django.urls import path
from app import views
urlpatterns = [
    path('', views.index),
    path('insert', views.insert),
    path('view', views.viewStudent),
    path('save', views.saveStdent),
]