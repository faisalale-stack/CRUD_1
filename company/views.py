from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer

def company(request):
	template = loader.get_template('company.html')
	return HttpResponse(template.render())

def customer(request):
	customers = Customer.objects.all()
	template = loader.get_template('customers.html')
	context = {'customers':customers,}
	return HttpResponse(template.render(context,request))

def customernew(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		address = request.POST["address"]

		data = Customer()

		data.first_name = first_name
		data.last_name = last_name
		data.email = email
		data.phone = phone
		data.address = address

		data.save()

		message = "<h1> New Customer</h1><p>New Customer created successfully <a href='/customers'>Customers</a> <p/>"
		return HttpResponse(message)

	
	return render(request, "customer_new.html",)

def customerupdate_old(request, pk):
	data = Customer.objects.get(pk =pk)
	data.first_name = "ooo"
	data.save()
	message = "<h1> Update Customer</h1><p>Customer updated successfully. Go back to <a href='/customers'>Customers</a> <p/>"
	return HttpResponse(message)

def customerupdate(request, pk):
	data = Customer.objects.get(pk =pk)

	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		address = request.POST["address"]

		data.first_name = first_name
		data.last_name = last_name
		data.email = email
		data.phone = phone
		data.address = address
		data.save()

		message = "<h1> Update Customer</h1><p>Customer updated successfully. Go back to <a href='/customers'>Customers</a> <p/>"
		return HttpResponse(message)



	context = {'data':data}
	return render(request,'customer_update.html',context)

def customerdelete(request,pk):
	data = Customer.objects.get(pk=pk)
	data.delete()

	message = "<h1> Delete Customer</h1><p>Customer deleted successfully. Go back to <a href='/customers'>Customers</a> <p/>"
	return HttpResponse(message)