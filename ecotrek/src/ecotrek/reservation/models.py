from __future__  import unicode_literals

from django.db import models



class reserve(models.Model):
	Full_Name	=	models.CharField(max_length=400)
	Email		=	models.EmailField(max_length=100)
	Inquiry_for	=	models.CharField(max_length=400)
	No_of_persons	=	models.CharField(max_length=400)
	Address	=	models.CharField(max_length=400)
	Country	=	models.CharField(max_length=400)
	Phone_no	=	models.CharField(max_length=400)
	Arrival_date	=	models.CharField(max_length=400)
	Departure_date	=	models.CharField(max_length=400)
	Other_specify	=	models.CharField(max_length=400)

	def __str__(self):
		return self.Full_Name
