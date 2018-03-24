from django.shortcuts import render

# Create your views here.

def login_view(request):
	return render(request,"form.html",{})

def register_view(request):
	return render(request,"form.html",{})

def logout_view(request):
	return render(request,"form.html",{})
