from django.urls import path

from . import views

app_name = 'recruit'
urlpatterns = [
    path('create/', views.create, name="create"),
    path('team-detail/<int:pk>/', views.team_detail, name="team-detail"),

]