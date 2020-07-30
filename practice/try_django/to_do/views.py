from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import *

# Create your views here.
def index(request):
	tasks=Task.objects.all()
	form=TaskForm()

	if request.method =="POST":
		form=TaskForm(request.POST)
		print("hello there")
		if form.is_valid():
			form.save()
		return redirect('/')
	context={

		'tasks':tasks,'form':form
		

	}
	return render(request,'to_do/base.html',context)


def updateTask(request,pk):
	task=Task.objects.get(id=pk)

	form=TaskForm(instance=task)

	if request.method=='POST':
		form=TaskForm(request.POST, instance=task)
		print("update")
		if form.is_valid():
			form.save()

		return redirect('/')
	context={
		'form':form
	}



	return render(request,'to_do/update.html',context)

def deleteTask(request,pk):
	item=Task.objects.get(id=pk)
	#form =TaskForm(instance=task)
	if request.method=="POST":
		#form=TaskForm(instance=task)
		item.delete()
		return redirect('/')

	context={
		'item':item
	}

	return render(request,'to_do/delete.html',context)
