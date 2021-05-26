from django.shortcuts import render,redirect
from .models import temperature,note
from .utils import getplot,getgraph,getplots
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
def viewfunction(request):
	data=temperature.objects.filter().all();	
	x_data=[str(x.Day) for x in data]
	y_data=[str(x.Temperature) for x in data]
	z_data=[str(x.Humidity) for x in data]
	chart=getplot(x_data,y_data)
	char=getplots(x_data,z_data)
	if request.method=="POST":
		day=request.POST["day"]
		z=temperature.objects.filter(Day=day)
		k=0
		tsum=0
		m=[]
		l=[]
		for i in x_data:
			if i==day and y_data[k]!="None":
				m.append(k)
			if i==day and z_data[k]!="None":
				l.append(k)
			k+=1
		if len(m)!=0:
			tsum=y_data[m[-1]]
		else:
			tsum=" "
		if len(l)!=0:
			hsum=z_data[l[-1]] 
		else:
			hsum=" "
		tlist=['21','22','23','24','25']
		hlist=['41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
		return render(request,"view.html",{'chart':chart,'char':char,'tsum':tsum,'hsum':hsum,'tlist':tlist,'hlist':hlist,}) 

	return render(request,"view.html",{'chart':chart,'char':char,})


def notesfunction(request):
	gmail=request.session["gmail"]
	data=note.objects.filter(Q(gmail=gmail))
	return render(request,'notes.html',{'data':data})

def addnotefunction(request):
	if request.method=="POST":
		gmail=request.session['gmail']
		text=request.POST['text']
		form=note()
		form.gmail=gmail
		form.text=text
		form.save()
		return redirect('notes')

def deletefunction(request,nid):
	data=note.objects.filter(id=nid).delete()
	return redirect('notes')

def logoutfunction(request):
	try:
		del request.session['gmail']
		return redirect('loginform')
	except KeyError:
		pass

