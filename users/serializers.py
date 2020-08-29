from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validate_data):
        user = User.objects.create_user(
            validate_data['username'], 
            validate_data['email'],
            validate_data['password'])

        return user    