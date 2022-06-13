from django.http.response import HttpResponse
from django.shortcuts import render
import rest_framework


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def todoList(request):
    querset =  Todo.objects.all()
    print("querset")
    print(querset)
    
    serializer = TodoSerializer(querset, many=True)
    print("serializer")
    print(serializer)
    
    return Response(serializer.data)

