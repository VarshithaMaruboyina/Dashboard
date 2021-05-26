from django.db import models

class register(models.Model):
	gmail=models.EmailField(max_length=100,blank=False,unique=True)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table="register"
# Create your models here.
