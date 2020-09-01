from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class ProfielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

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
            validate_data['first_name'],
            validate_data['last_name'],
            validate_data['username'], 
            validate_data['email'],
            validate_data['password'])

        return user    

    def update(self, instance, validate_data):
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.username = validate_data.get('username', instance.first_name)
        instance.email = validate_data.get('email', instance.email)
