from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework import status
from receipe.serializers import UserSerializer
from django.contrib.auth.models import User
from receipe.models import receipes
from receipe.serializers import ReceipeSerializer
# Create your views here.
class UserCreate(APIView):
	def post(self,request,format='json'):
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				return Response(serializer.data,status=status.HTTP_201_CREATED)
def index(request):
	return HttpResponse("Hello world")

def receipe_create_listAll(request):
	if request.method == 'GET':
		receipe = receipes.objects.all()
		serializer = ReceipeSerializer(receipe,many=True)
		return JsonResponse(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ReceipeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.error,status=400)

def  receipe_modify_user(request,user):
	try:
		receipe = receipes.objects.get(user=user)
	except receipes.DoesNotExist:
		return HttpResponse(status=404)
	if reuest.method == 'GET':
		serializer = ReceipeSerializer(receipe)
		return JsonResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ReceipeSerializer(receipe,data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.error,status=400)
	elif reuest.method == 'DELETE':
		receipe.delete()
		return HttpResponse(status=204)
