from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


from account.forms import *
from aba_app.models import Stage
from account.models import *


# Create your views here.
def logout_view(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print(username, password)
            messages.success(request, ("There was an error loging you in"))
            return redirect('login')
            user = form.get_user()
            login(request, user)
            print("OK")
            return redirect('index.html')

    return render(request, 'account/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print(username, password)
            messages.success(request, ("There was an error loging you in"))
            return redirect('login')
            user = form.get_user()
            login(request, user)
            print("OK")
            return redirect('index.html')
    else:

        return render(request, 'account/login.html')

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
    return render(request, 'account/register.html', {'form': form})


@login_required(login_url='login')
def edit_user_profile(request, id):
    user = User.objects.get(id=id)
    form = editUserPofile(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('view_profile')

    return render(request, 'account/profile_edit.html', {'form': form})


def view_profile(request,id):
    user = User.objects.get(id=id)
    userSetting = UserSetting.objects.get(user=id)

    context ={
        'user':user,
        'userSetting':userSetting

    }

    return render(request, 'account/profile_setting.html',context)
