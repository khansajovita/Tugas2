import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TodoForm

# Create your views here.

@login_required(login_url='/todolist/login/')

def show_todolist(request):
    list = Task.objects.filter(user = request.user)
    context = {'list': list}
    return render(request, "todolist.html", context)

def create_task(request):
    list = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = Task()
            obj.user = request.user
            obj.title = form['judul'].value()
            obj.description = form['deskripsi'].value()
            obj.date = datetime.datetime.now()
            obj.save()
            messages.success(request, 'Sudah berhasil ditambahkan!')
            return redirect('todolist:show_todolist')

    form = TodoForm()
    page = {
             "forms" : form,
             "list" : list,
           }
    return render(request, 'createtask.html', page)

def change_status(request):
    list = Task.objects.filter(user = request.user)
    for i in list:
        if request.POST.get(str(i.id)):
            i.is_finished = not i.is_finished
            i.save()
    return redirect('todolist:show_todolist')

def delete(request):
    list = Task.objects.filter(user = request.user)
    for i in list:
        if request.POST.get(str(i.id)):
            i.delete()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))      
            return response  
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')