from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed

from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token


class RegisterAPIView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request):
        user = CustomUser.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return access_token
        # return Response({
        #     'token': access_token
        # })

class UserAPIView(APIView):
    def get(self, request):
        token = RefreshAPIView.post(self, request)

        if token:
            id = decode_access_token(token)
            user = CustomUser.objects.filter(pk=id).first()
            return Response(CustomUserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')

class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response




# CREATE NEW USER VIA API

class CreateCustomUser(generics.CreateAPIView):
    '''
    CURL COMMAND TO CREATE NEW USER
    curl --data "email=newuser@pp.com&first_name=newuserfirstname&last_name=newuserfirstname&password=1234" http://127.0.0.1:8000/register/

    URL: http://127.0.0.1:8000/register/
    '''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# API ENDPOINT TO SHOW ACCOUNT DETAILS FOR LOGGED-IN USER USING CUSTOMUSER SERIALIZER

class ViewUserAccount(generics.ListAPIView):
    '''
    VIEW ACCOUNT INFO FOR LOGGED IN USER:\n
    URL: 'http://127.0.0.1:8000/viewuseraccount/'
    
    '''
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        logged_in_user = self.request.user.id  
        queryset = CustomUser.objects.filter(id = logged_in_user)
        return queryset


# ADMIN VIEW TO SHOW ACCOUNT DETAILS FOR SPECIFIC USER ID
class AdminViewUser(generics.ListAPIView):
    '''
    VIEW ACCOUNT INFO FOR SPECIFIC USER. (in the case below details of user with id 8 will be shown):
    http://127.0.0.1:8000/adminviewuser/8/

    I HAVE ALSO CONFIGURED DJANGO ADMIN URL TO DO SAME THING: 
    http://127.0.0.1:8000/admin/
    
    '''
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
        
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = CustomUser.objects.filter(id = id)
        return queryset