from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home, name='home'),
    path('get-student/' , get_student ,name='get_student'),
    path('post-student/' , post_student ,name='post_student'),
    path('put-student/<id>/' , put_student ,name='put_student'),
    path('delete-student/<id>/' , delete_student ,name='delete_student'),
    path('get-books/' , get_books ,name='get_books')
     
]