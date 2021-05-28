from django.urls import path
from todos import views

urlpatterns = [
    path('delete/<int:pk>', views.delete_todo_item, name='delete_todo_item'),
    path('', views.todo_list_item, name='home'),
]
