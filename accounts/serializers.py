from rest_framework import serializers

from . models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('name', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


