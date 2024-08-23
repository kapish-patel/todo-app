from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


class TodoApi(APIView):
    def get(self, request):
        # get the user id from the request path
        userId = request.GET.get('userId')
        # get the todos for the user
        todos = Todo.objects.filter(userId=userId)
        # serialize the todos
        serializer = TodoSerializer(todos, many=True)
        # return the serialized data
        return Response(serializer.data)
    
    def post(self, request):
        # serialize the request data
        serializer = TodoSerializer(data=request.data)
        # validate the data
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error response
        return Response(serializer.errors, status=400)
    
    def put(self, request):
        # get the todo id from the request path
        print(request.data)
        id = request.data['id']
        # get the todo
        todo = Todo.objects.get(id=id)

        
        # serialize the request data
        serializer = TodoSerializer(todo, data=request.data)
        # validate the data
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error response
        return Response(serializer.errors, status=400)

    def delete(self, request):
        # delete the todo and return the same todo with id
        id = request.data['id']
        todo = Todo.objects.get(id=request.data['id'])
        todo.delete()
        serializer = TodoSerializer(todo)
        # prepare the response data with the id and the serialized data
        responseData = {
            'id': id,
            'data': serializer.data
        }
        return Response(responseData)
    