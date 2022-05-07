
from django.urls import path

from todo_app import views

urlpatterns = [
    
    path('index/', views.index , name='index'),
    path('add/', views.add , name='add'),
    
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('is_completed/<int:id>', views.is_completed, name='is_completed')
]