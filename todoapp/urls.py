from django.urls import path
from .views import HomeView, todo_List_View, todo_item_create,delete_todo_item

app_name = 'todoapp'
urlpatterns = [
    path('',HomeView,name='home_url'),
    path('list/',todo_List_View,name='todo_list'),
    path('create/',todo_item_create,name='todo_item_create'),
    path('<id>/delete/',delete_todo_item ,name='todo_item_delete'),
]