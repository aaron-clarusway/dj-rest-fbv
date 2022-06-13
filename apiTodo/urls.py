from django.urls import path
from .views import home, hello_world, todoList, todoCreate


urlpatterns = [
    path('', home),
    path('hello/', hello_world),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    
]
