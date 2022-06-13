from django.http.response import HttpResponse
from django.shortcuts import render
import rest_framework
from rest_framework import serializers


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
    serializer = TodoSerializer(querset, many=True)
   
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)