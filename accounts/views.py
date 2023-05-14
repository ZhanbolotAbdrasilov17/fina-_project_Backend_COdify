from django.contrib.auth import get_user_model

from . serializers import UserSerializer

User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)

                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})


class UserUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        name = request.data.get('name')
        email = request.data.get('email')
        if name and email:
            user.name = name
            user.email = email
            user.save()
            serializer = UserSerializer(user, context=self.get_renderer_context()).data
            return Response(serializer, status=status.HTTP_200_OK)
        return Response('name and email is required!', status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user, context=self.get_renderer_context()).data
        return Response(serializer, status=status.HTTP_200_OK)
