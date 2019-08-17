from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class step(models.Model):
	step_text = models.CharField(max_length=400,null=False)

class ingredient(models.Model):
	text = models.CharField(max_length=400,null=False)

class receipes(models.Model):
	name = models.CharField(max_length=80,null=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Step= models.ForeignKey(step, related_name='receipe_steps',on_delete=models.CASCADE)
	Ingredient= models.ForeignKey(ingredient, related_name='receipe_ingredients',on_delete=models.CASCADE)
