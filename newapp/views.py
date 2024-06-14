from django.shortcuts import render, redirect
from .models import Member

def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    if request.method == 'POST':
        x = request.POST['first']
        y = request.POST['last']  # Corrected
        z = request.POST['country']  # Corrected
        mem = Member(firstname=x, lastname=y, country=z)
        mem.save()
        return redirect("/")

def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    if request.method == 'POST':
        mem = Member.objects.get(id=id)  # Retrieve the member object based on id
        x = request.POST['first']
        y = request.POST['last']
        z = request.POST['country']
        mem.firstname = x
        mem.lastname = y
        mem.country = z
        mem.save()
        return redirect("/")
