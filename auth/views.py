from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.views import APIView
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class GetView(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer = RegisterSerializer(user,many=True)
        return Response(serializer.data)

class GetListView(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        user = self.get_object(id)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
    
    def put(self,request,id):
        user = self.get_object(id)
        serializer = RegisterSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

# class ChangePasswordView(APIView):
    # def post(self,request):
    #     serializer = ChangePasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    # def get_object(self,id):
    #     try:
    #         return User.objects.get(id=id)
    #     except User.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    # def get(self,request,id):
    #     user = self.get_object(id)
    #     serializer = ChangePasswordSerializer(user)
    #     return Response(serializer.data)
    
    # def put(self,request,id):
    #     user = User.objects.get(id)
    #     serializer = ChangePasswordSerializer(user,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
