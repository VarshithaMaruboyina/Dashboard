from django.shortcuts import render,redirect
from .models import register
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
# Create your views here.
def registerfunction(request):
	return render(request,'register.html')

def registerdatafunction(request):
	if request.method=="POST":
		try:
			form=register()
			form.gmail=request.POST['gmail']
			form.password=request.POST['pwd']
			form.save()
			return redirect('loginform')
		except Exception as e:
			return render(request,'register.html',{'msg':"1",})
def loginfunction(request):
	return render(request,'login.html')

def logincheckfunction(request):
	if request.method=="POST":
		gmail=request.POST['gmail']
		pwd=request.POST['pwd']
		check=register.objects.filter(Q(gmail=gmail)&Q(password=pwd))
		if check:
			request.session['gmail']=gmail;
			return redirect('view')
		else:
			return render(request,'login.html',{'msg':"1",})
