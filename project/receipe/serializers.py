from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.models import User
from receipe.models import receipes, step, ingredient
class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
	first_name = serializers.CharField(max_length=200)
	last_name = serializers.CharField(max_length=200)
	password = serializers.CharField(min_length=8, write_only=True)
	def create(self,validated_data):
		user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
		return user
	class Meta:
		model = User
		fields = ('id','username','email','first_name','last_name','password')

class ReceipeSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	receipe_steps = serializers.RelatedField(source='Step',queryset=step.objects.all())
	receipe_ingredients = serializers.RelatedField(source='Ingredient',queryset=ingredient.objects.all())
	class Meta:
		model = receipes
		fields = ('name','user','receipe_steps','receipe_ingredients')
