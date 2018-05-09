from django.shortcuts import render, redirect

from django.http import Http404
from django.contrib import messages
from . models import Hotel, HotelBooking

def hotellist(request):
	qs=Hotel.objects.all()
	context={
		'obj_list':qs,
	}

	return render(request,'hotellist.html',context)

def hoteldetails(request,id):
	qs= Hotel.objects.get(id=id)
	context={
		'obj_list':qs
	}
	return render(request,'hoteldetails.html',context)


def  add_hotel(request):
	if (request.method=='POST'):
		HotelName=request.POST['HotelName']
		HotelStars=request.POST['HotelStars']
		Address=request.POST['Address']
		data = Hotel(	HotelName=HotelName,
						HotelStars=HotelStars,
						Address=Address,
						)
		data.save()
		return redirect('/admin')

	else:
		return render(request,'add_hotel.html')



def hotel_reservation(request,id):
	qs= Hotel.objects.get(id=id)
	context={
		'obj_list':qs
	}
	if (request.method=='POST'):
		hotel=request.POST['hotel']
		adults=request.POST['adults']
		child=request.POST['child']
		full_name=request.POST['full_name']
		email=request.POST['email']
		address=request.POST['address']
		phone=request.POST['phone']
		check_in_date=request.POST['check_in_date']
		check_out_date=request.POST['check_out_date']
		single_room=request.POST['single_room']
		extra_bed=request.POST['extra_bed']
		double_room=request.POST['double_room']
		accomodation_type=request.POST['accomodation_type']
		message=request.POST['message']

		data =HotelBooking(	hotel=hotel,
							adults=adults,
							child=child,
							full_name=full_name,
							email=email,
							address=address,
							phone=phone,
							check_in_date=check_in_date,
							check_out_date=check_out_date,
							single_room=single_room,
							double_room=double_room,
							extra_bed=extra_bed,
							accomodation_type=accomodation_type,
							message=message,
						)
		data.save()
		return redirect('/')

	else:
		return render(request,'book-now.html',context)


def hotel_reservation_list(request):
	qs=HotelBooking.objects.all()
	context={
		'obj_list':qs
	}
	return render(request,'hotel-reservatioin-request.html',context)

def hotel_reservation_details(request,id):
	qs= HotelBooking.objects.get(id=id)
	context={
		'obj_list':qs
	}
	return render(request,'hotel-reservation-details.html',context)


def edit_hotel(request, id):
	qs= Hotel.objects.get(id=id)
	context={
		'obj_list':qs
	}
	if (request.method=='POST'):
		HotelName=request.POST['HotelName']
		HotelStars=request.POST['HotelStars']
		Address=request.POST['Address']
		data = Hotel(	id=id,
						HotelName=HotelName,
						HotelStars=HotelStars,
						Address=Address,
						)		
		if data is not None:
			data.save()
			return redirect('/hotel/hotellist')
	else:
		return render(request,'edit_hotel.html', context)

def delete_hotel(request, id):
	if not request.user.is_superuser:
		raise Http404
	qs= Hotel.objects.get(id=id)
	context={
		'obj_list':qs
	}
	qs.delete()
	return redirect('/hotel/hotellist')

