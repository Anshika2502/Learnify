from django.shortcuts import render , redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request , 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # get form input values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                #that username is taken
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    #that email is being used
                    return redirect('register')
                else:
                    #create a new user
                    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    #you are new registered and can login
                    return redirect('login') 
        else:
            #passwords don't match
            return redirect('register')
    else:
        return render(request , 'accounts/register.html')

def logout(request):
    return redirect('course-list')