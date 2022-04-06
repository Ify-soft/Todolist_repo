from django.contrib import admin
from django.urls import path
from .views import home, todoview, analyseViews
 
app_name='todo'
urlpatterns = [
    path('', home, name='home'),
    path("todolist/", todoview.as_view(), name='todoform'),
    path("todolist/grade/", analyseViews.as_view(), name='updateform'),
]
