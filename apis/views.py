from django.shortcuts import render,redirect
from .models import gameInfo
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def home(request):
	id_count = -1
	if 'start' in request.GET:
		id_count = gameInfo.objects.all().count()
		messages.success(request,f'READY !')
		return redirect('/'+str(id_count+1))
	args = {'count':id_count}	
	return render(request,'home.html',args)

def start(request,idi):
	try:
		info = gameInfo.objects.get(id=idi)
		# print(info.result)
		dict1 = {'Game Id':info.id,'Game Result':info.result}
		return JsonResponse(dict1)
	except:
		form_obj = gameInfo(idi,'-').save()
		return render(request,'game.html')

def update_status(request,idi,p):
	# if request.POST:
	inf = gameInfo.objects.get(id=idi)
	inf.result = 'Player '+str(p)
	inf.save()
	messages.success(request,f'Player '+str(p) +' wins !')
	return redirect('/'+str(idi+1))	

# def start(request):



