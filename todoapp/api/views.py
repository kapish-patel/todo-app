from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


class TodoApi(APIView):
    def get(self, request):
        # fetch data from the database and return it in json format
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({'todos': serializer.data})
    
    def post(self, request):
        # create a new todo and return a response
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'todo': serializer.data})
        else:
            return Response(serializer.errors)
    
    def put(self, request):
        # Update a todo and return a response
        todo = Todo.objects.get(id=request.data['id'])
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'todo': serializer.data})
        else:
            return Response(serializer.errors)
        
    
    def delete(self, request):
        # delete a todo and return a response
        todo = Todo.objects.get(id=request.data['id'])
        todo.delete()
        return Response({'message': 'Todo deleted', 
                         'status': True})
