from django.urls import path
from .views import home, hello_world, todoList


urlpatterns = [
    path('', home),
    path('hello/', hello_world),
    path('todoList/', todoList),
    
]
