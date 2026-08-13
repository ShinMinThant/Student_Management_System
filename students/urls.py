from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),

    path('<int:id>/', views.student_detail, name='student_detail'),
    path('<int:id>/edit/', views.edit_student, name='edit_student'),
    path('<int:id>/delete/', views.delete_student, name='delete_student'),
]