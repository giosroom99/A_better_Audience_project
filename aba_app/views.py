from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("OK")
            return redirect('index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'common/login.html', {"Login_form": form})

def logout_view(request):
    logout(request)
    form = AuthenticationForm(request.POST)
    return render(request, 'common/login.html', {"Login_form": form})
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

        return render(request, 'common/login.html')

def index(request):
    return render(request, 'main/index.html')

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




def handle_uploaded_file(f):
    with open(''
              'media/stage_images/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



""" ################################################
Presentations Views
""" ##############################################


def presentation_views(request):
    presentations = Presentation.objects.all()
    context = {'Stages': presentations}
    return render(request, 'presentations/presentations.html', context)

def updatePresentation_view(request, id):
    presentation = Presentation.objects.get(id=id)
    form = CreatePresentationForm(request.POST or None, instance=presentation)
    if form.is_valid():
        form.save()
        return redirect('stage')
    return render(request, 'presentations/create_presentation.html', {'form': form})

def deletePresentation_view(request):
    return None
def PresentationDetail_view(request):
    return None
def create_presentation_views(request):
    submitted = False
    if request.method == 'POST':
        presentation_form = CreatePresentationForm(request.POST, request.FILES)
        if presentation_form.is_valid():
            presentation_form.save()
            return HttpResponseRedirect('/create_presentation')
    else:
        presentation_form = CreatePresentationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'presentations/create_presentation.html',
                  {'presentation_form': presentation_form, 'submitted': submitted})


""" ######################################################### STAGE

The Function below is use to update stage details. when the user 
click on the stage name it brings them to 
the form and filer to only update the stage that was clicked. 
This is possible because we are passing the PK 
as a parameter to the view function
"""#############################################################
def updateStage_view(request, id):
    stage = Stage.objects.get(id=id)
    form = CreateStageForm(request.POST or None, instance=stage)
    if form.is_valid():
        form.save()
        return redirect('stage')
    return render(request, 'stage/create_stage.html', {'add_stageForm': form, })


def deleteStage_view(request, id):
    stage = Stage.objects.get(id=id)
    if request.method == "POST":
        stage.delete()
        return redirect('stage')

    return render(request, 'stage/delete-confirm.html', {'stage': stage, })


def stageDetail_view(request, id):
    presentations = Presentation.objects.filter(stage=id)
    print(presentations)
    stage = Stage.objects.get(id=id)
    # print(stage+ """""""""""""""""""""""""")
    context = {'stage': stage, 'presentations': presentations}
    return render(request, 'stage/view_stage.html', context)

def add_stage_view(request):
    submitted = False
    if request.method == 'POST':
        add_stageForm = CreateStageForm(request.POST, request.FILES)
        if add_stageForm.is_valid():
            # handle_uploaded_file(request.FILES["Stage_image"])
            add_stageForm.save()
            return HttpResponseRedirect('/add_stage')
    else:
        add_stageForm = CreateStageForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'stage/create_stage.html', {'add_stageForm': add_stageForm, 'submitted': submitted})

def stage_view(request):
    stages = Stage.objects.all()
    context = {'Stages': stages}
    return render(request, 'stage/stage.html', context)
