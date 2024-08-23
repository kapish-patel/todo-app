
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IdentitySerializer
from .models import Identity


class IdentityApi(APIView):
    # validate the request data and create a new identity
    def post(self, request):

        if request.path == '/identity/login/':
            return self.login(request)

        # check if the email is already in use
        email = request.data['email']
        if Identity.objects.filter(email=email).exists():
            return Response({'message': 'Email already in use', 
                             'status': False})
        
        # create defaule categories
        request.data['categories'] = ['Personal', 'Work', 'Shopping', 'Home', 'Others']

        serializer = IdentitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'identity': serializer.data})
        else:
            return Response(serializer.errors)
    
    def login(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        try:
            identity = Identity.objects.get(email=email)
            if identity.check_password(password):
                serializer = IdentitySerializer(identity)
                return Response({'identity': serializer.data})
            else:
                return Response({'message': 'Invalid credentials', 
                                 'status': False})
        except Identity.DoesNotExist:
            return Response({'message': 'Invalid credentials', 
                             'status': False})
        
    # update the identity and return a response
    def put(self, request):
        identity = Identity.objects.get(email=request.data['email'])
        
        request.data['password'] = identity.password
        
        serializer = IdentitySerializer(instance=identity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'identity': serializer.data})
        else:
            return Response(serializer.errors)