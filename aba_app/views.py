from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AudienceUserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def presentation_views(request):
    return render(request, 'presentations/presentations.html')


def create_presentation_views(request):
    return render(request, 'presentations/create_presentation.html')


def stage_view(request):
    return render(request, 'stage/stage.html')


# This function renders the registration form page and create a new page based on the form data
def register_view(request):
    if request.method == 'POST':
        form = AudienceUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # password1= form.changed_data['']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'main/index.html')
    else:
        form = AudienceUserRegistrationForm()
    return render(request, 'common/register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             print("OK")
#             return redirect('index.html')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'common/login.html', {"Login_form": form})
def logout_view(request):
    logout(request)
    form = AuthenticationForm(request.POST)
    return render(request, 'common/login.html', {"Login_form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            print(username, password)
            messages.success(request,("There was an error loging you in"))
            return redirect('login')
            user = form.get_user()
            login(request, user)
            print("OK")
            return redirect('index.html')
    else:

        return render(request, 'common/login.html')