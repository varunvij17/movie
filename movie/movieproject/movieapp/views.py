from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from . forms import MovieForm

# Create your views here.
def index(request):
    mov=movie.objects.all()
    context={
        'movielist':mov
    }

    return render(request,'index.html',context)

def detail(request,movieid):
    mov=movie.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':mov})

def addmovie(request):
    if request.method=="POST":
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        year = request.POST.get('year', )
        image = request.FILES['image']
        mov = movie(name=name,description=description,year=year,image=image)
        mov.save()

    return render(request,'add.html')

def update(request,updateid):
    mov=movie.objects.get(id=updateid)
    form=MovieForm(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mov':mov})

def delete(request,deleteid):
    if request.method=="POST":
        mov=movie.objects.get(id=deleteid)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')
