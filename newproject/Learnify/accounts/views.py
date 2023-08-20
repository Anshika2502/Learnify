from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('course-list')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            print('You are now logged in')
            return redirect('course-list')
        print('Invalid credentials')
        return redirect('login')

    return render(request , 'accounts/login.html')

def register(request):

    if request.user.is_authenticated:
        return redirect('course-list')
    
    if request.method == 'POST':
        # get form input values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
             #passwords don't match
            return redirect('register')
        if User.objects.filter(username=username).exists():
             #that username is taken
             return redirect('register')
        if User.objects.filter(email=email).exists():
             #that email is being used
             return redirect('register')
        
        user = User.objects.create_user(username=username, email=email,password=password_1, first_name=first_name, last_name=last_name)
        user.save()
        #you are new registered and can login
        return redirect('login')
           
    return render(request , 'accounts/register.html')

def logout(request):
    auth.logout(request)
    #you are now logged out 
    return redirect('course-list')

@login_required(login_url='/accounts/login')
def my_profile(request):

    if request.method =='POST':
        user = request.user
        user.email = request.POST['email']
        user.username = request.POST['username']
        student_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.student)

        if student_form.is_valid():
            student_form.save()
            user.save()
            #your account has been updated
            return redirect('my_profile')

    student_form = UpdateProfileForm(instance=request.user.student)

    context = {
        'student' : request.user.student , 
        'student_form' : student_form
    }
    return render(request , 'accounts/my_profile.html' , context)