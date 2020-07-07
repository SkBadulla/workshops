from django.db import models

# Create your models here.

class Workshop_Details(models.Model):
	name_of_workshop = models.CharField(max_length=100) 
	organized_by = models.CharField(max_length=150)
	duration  = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	

	 
class UploadImage(models.Model):
	username = models.CharField(max_length=50)
	imgup = models.ImageField(upload_to='images/')