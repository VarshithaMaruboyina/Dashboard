from django.db import models

# Create your models here.
class temperature(models.Model):
	Time=models.CharField(max_length=30)
	Temperature=models.CharField(max_length=30)
	Humidity=models.CharField(max_length=30)
	Day=models.CharField(max_length=30)
	class meta:
		db_table="temperature"


class note(models.Model):
	gmail=models.EmailField(max_length=100,blank=False)
	time = models.DateTimeField(auto_now_add=True)
	text =models.CharField(max_length=1000,blank=False)
	class Meta:
		db_table="note"
