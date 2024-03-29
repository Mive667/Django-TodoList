from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('mark_as_completed/<int:pk>', views.mark_as_completed, name='mark_as_completed'),
    path('mark_as_uncompleted/<int:pk>', views.mark_as_uncompleted, name='mark_as_uncompleted'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]