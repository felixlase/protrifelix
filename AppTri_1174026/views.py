from django.shortcuts import render
from django.http import HttpResponse
from AppTri_1174026.forms import NewUserForm
# Create your views here.

def index(request):
	return render(request,'index_1174026.html')

def halform(request):
	form = NewUserForm(request.POST)
	if request.method == "POST":

		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
		else :
			print("ERROR FORM INVALID")
	return render(request, 'index_1174026.html',{'form':form})