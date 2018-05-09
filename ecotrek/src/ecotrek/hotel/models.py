from django.db import models

# Create your models here.
class Hotel(models.Model):
	HotelName	=	models.CharField(max_length=400)
	HotelStars	=	models.CharField(max_length=400)
	Address		=	models.CharField(max_length=400)

	def __str__(self):
		return self.HotelName

class HotelBooking(models.Model):
	hotel	=	models.CharField(max_length=400)
	adults	=	models.CharField(max_length=400)
	child	=	models.CharField(max_length=400)
	full_name	=	models.CharField(max_length=400)
	email	=	models.CharField(max_length=400)
	address	=	models.CharField(max_length=400)
	phone	=	models.CharField(max_length=400)
	check_in_date	=	models.CharField(max_length=400)
	check_out_date	=	models.CharField(max_length=400)
	single_room	=	models.CharField(max_length=400)
	double_room	=	models.CharField(max_length=400)

	extra_bed	=	models.CharField(max_length=400)
	accomodation_type	=	models.CharField(max_length=400)
	message	=	models.CharField(max_length=400)

