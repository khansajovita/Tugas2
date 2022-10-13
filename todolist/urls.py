
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('change-status', change_status, name='change_status'),
    path('delete', delete, name='delete'),
    path('json', show_ajax, name='show_ajax'),
    path('add', todolist_ajax, name='todolist_ajax'),
]