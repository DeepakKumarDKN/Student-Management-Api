from django.urls import path
from api import views

urlpatterns = [
    path('student/',views.StudentListView.as_view()),
    path('student_create/', views.StudentListCreateView.as_view()),
    
    path('student_detail/<int:pk>/',views.StudentDetailView.as_view()),
    path('student_update/<int:pk>/', views.StudentUpdateView.as_view()),
    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view())
]
