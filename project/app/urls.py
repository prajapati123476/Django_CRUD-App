from django.urls import path
from app import views
urlpatterns = [
    path('', views.index),
    path('insert', views.insert, name="insert"),
    path('view', views.viewStudent),
    path('save', views.saveStdent, name="save_student"),
]