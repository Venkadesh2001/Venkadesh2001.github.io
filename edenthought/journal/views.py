from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm,Create_Thought,UpdateUserForm,UpdateProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import CreateThought,Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def homepage(request):
    return render(request,'journal/index.html')




def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit = False)
            form.save()
            send_mail('Welcome to Eden Thoughts','Your Registration was successfull',settings.DEFAULT_FROM_EMAIL,[current_user.email])
            profile = Profile.objects.create(user = current_user)
            messages.success(request,'User Created')
            return redirect('my-login')


    context = {'registeruser':form}
    return render(request,'journal/register.html',context)



def my_login(request):
    form = LoginForm()
    if request.method=="POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    context = {'loginpage':form}
    return render(request,'journal/login.html',context)



@login_required(login_url = 'my-login')
def dashboard(request):
    profilePicture = Profile.objects.get(user=request.user)
    context = {'profilePicture':profilePicture}
    return render(request,'journal/dashboard.html',context)


@login_required(login_url = 'my-login')
def create_thought(request):
    form  = Create_Thought()
    if request.method == 'POST':
        form = Create_Thought(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return redirect('view-thought')

    context = {'createthought':form}
    return render(request,'journal/create-thought.html',context)


@login_required(login_url = 'my-login')
def view_thoughts(request):
    current_user = request.user.id
    thought = CreateThought.objects.all().filter(user = current_user)
    context = {'viewThought':thought}
    
    return render(request,'journal/view-thought.html',context)


@login_required(login_url = 'my-login')
def update_thought(request,pk):
    try:
        thought = CreateThought.objects.get(id = pk,user = request.user)
    except:
        return redirect('view-thought')
    form = Create_Thought(instance = thought)
    if request.method =="POST":
        form = Create_Thought(request.POST,instance = thought)
        if form.is_valid():
            form.save()
            return redirect('view-thought')


    context = {'updateThought':form}
    return render(request,'journal/update-thought.html',context)


@login_required(login_url = 'my-login')
def delete_thought(request,pk):
    try:
        thought = CreateThought.objects.get(id=pk,user = request.user)

    except:
        return redirect('view-thought')
    
    if request.method=='POST':
        thought.delete()
        return redirect('view-thought')


    return render(request,'journal/delete-thought.html',)


@login_required(login_url = 'my-login')
def profile_management(request):
    form = UpdateUserForm(instance = request.user)
    profile = Profile.objects.get(user = request.user)
    form_2 = UpdateProfileForm(instance = profile)
    if request.method == "POST":
        form = UpdateUserForm(request.POST,instance = request.user)
        form_2 = UpdateProfileForm(request.POST,request.FILES,instance = profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        if form_2.is_valid():
            form_2.save()
            return redirect('dashboard')

    context = {'usernameUpdateForm':form,'profileUpdateForm':form_2}
    return render(request,'journal/profile-management.html',context)


@login_required(login_url = 'my-login')
def delete_account(request):
    if request.method=="POST":
        deleteUser = User.objects.get(username = request.user)
        deleteUser.delete()
        return redirect('')

    return render(request,'journal/delete-account.html',)


























def logout(request):
    auth.logout(request)
    return redirect('')