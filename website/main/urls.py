from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('teams/', views.teams, name='main-teams'),
    path('draft/', views.draft, name='main-draft'),
    path('weeklyStats/', views.weeklyStats, name='main-weeklyStats'),
    path('weeklyStats/week1/', views.week1, name='main-week1'),
    path('weeklyStats/week2/', views.week2, name='main-week2'),
    path('weeklyStats/week3/', views.week3, name='main-week3'),
    path('weeklyStats/week4/', views.week4, name='main-week4'),
    path('weeklyStats/week5/', views.week5, name='main-week5'),
    path('weeklyStats/week6/', views.week6, name='main-week6'),
    path('weeklyStats/week7/', views.week7, name='main-week7'),
    path('weeklyStats/week8/', views.week8, name='main-week8'),
    path('weeklyStats/week9/', views.week9, name='main-week9'),
    path('weeklyStats/week10/', views.week10, name='main-week10'),
    path('weeklyStats/week11/', views.week11, name='main-week11'),
    path('weeklyStats/week12/', views.week12, name='main-week12'),
    path('weeklyStats/week13/', views.week13, name='main-week13'),
    path('weeklyStats/week14/', views.week14, name='main-week14'),
    path('weeklyStats/week15/', views.week15, name='main-week15'),
    path('weeklyStats/week16/', views.week16, name='main-week16'),
    path('weeklyStats/week17/', views.week17, name='main-week17'),
]