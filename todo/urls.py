from django.contrib import admin
from django.urls import path
from .views import home, todoview, display_function, process_function, profile_page, get_todolist_by_date,\
 get_todolist_for_today, profileUpdateView, daily_score_graph
 
app_name='todo'
urlpatterns = [
    path('', home, name='home'),
    path("todolist/", todoview.as_view(), name='todoform'),
    #path("todolist/grade/<slug:slug>/", analyseViews.as_view(), name='updateform'),
    path("todolist/grade/", display_function, name='updateform'),
    path("todolist/grade/response", process_function, name='responseform'),
    path("profile/", profile_page.as_view(), name="profile_page"),
    path("profile/allList/", get_todolist_by_date, name="listPerDay"),
    path("profile/oneList/", get_todolist_for_today, name="listToday"),
    path("profile/oneList/", get_todolist_for_today, name="listToday"),
    path("profile/<int:pk>/", profileUpdateView, name="profileEdit"),
    path("profile/stat/", daily_score_graph, name="statGraph")
]
