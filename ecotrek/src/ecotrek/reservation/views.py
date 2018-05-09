from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import reserve




def index(request):
	qs=reserve.objects.all()
	context={
		'obj_list':qs
	}
	return render(request,'reservation/add.html',context)

def list_view(request):
	qs=reserve.objects.all()
	a= reserve.objects.filter(Full_Name__iexact='man')
	context={
		'obj_list':qs,
	}

	return render(request,'reservation/list.html',context)

def details(request,id):
	qs= reserve.objects.get(id=id)
	context={
		'obj_list':qs
	}
	return render(request,'reservation/details.html',context)



def add(request):
	if (request.method=='POST'):
		Full_Name=request.POST['fullname']
		Email=request.POST['email']
		Inquiry_for=request.POST['Inquiry_for']
		No_of_persons=request.POST['No_of_persons']
		Address=request.POST['Address']
		Country=request.POST['Country']
		Phone_no=request.POST['Phone_no']
		Arrival_date=request.POST['Arrival_date']
		Departure_date=request.POST['Departure_date']
		Other_specify=request.POST['Other_specify']

		data = reserve(	Full_Name=Full_Name,
						Email=Email,
						Inquiry_for=Inquiry_for,
						No_of_persons=No_of_persons,
						Address=Address,
						Country=Country,
						Phone_no=Phone_no,
						Arrival_date=Arrival_date,
						Departure_date=Departure_date,
						Other_specify=Other_specify,
						)
		data.save()
		return redirect('/reservation/a')

	else:
		return render(request,'reservation/add.html')
