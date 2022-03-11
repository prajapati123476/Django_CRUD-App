from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insert, name="insert"),
    path('view', views.viewStudent, name="view"),
    path('save', views.saveStdent, name="save_student"),
    path('updateStudent', views.updateStudent, name="updateStudent"),
    path('update', views.update, name="update"),
]