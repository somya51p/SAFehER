from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup1(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        r = request.POST['role']
        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c,role=r)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'signup.html', d)

def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    d = {'data':data, 'user':user}
    return render(request, 'profile.html', d)

@login_required
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    error = False
    if request.method == 'POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        c=request.POST['contact']
        u=request.POST['username']
        user.first_name = f
        user.last_name = l
        data.contact = c
        user.username = u
        user.save()
        data.save()
        error=True
    d = {'data':data, 'user':user, 'error':error}
    return render(request, 'edit_profile.html', d)

@login_required
def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method == 'POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username__exact = request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request, 'changepassword.html',d)

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)

@staff_member_required(login_url='/login_admin/')
def admin_home(request):
    return render(request, 'admin_home.html')

@staff_member_required(login_url='/login_admin/')
def view_users(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    users = Signup.objects.all()

    d = {'users':users}
    return render(request, 'view_users.html',d)

@staff_member_required(login_url='/login_admin/')
def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect('view_users')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

@login_required
def menstrual(request):
    return render(request, 'menstrual.html')

@login_required
def bmi(request):
    return render(request, 'bmi.html')

@login_required
def browse(request):
    return render(request, 'browse.html')

@login_required
def vaccine(request):
    return render(request, 'vaccine.html')

@login_required
def upload_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,status="pending")

            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'upload_queries.html')