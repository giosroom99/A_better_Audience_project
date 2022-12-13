import json

from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect

from django.db.models import Sum, Avg
from .forms import *
from .models import *

from django.http import HttpResponseRedirect


@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')


""" ################################################
                    Presentations Views
    ##############################################
"""


@login_required(login_url='login')
def presentation_views(request, id):
    presentations = Presentation.objects.filter(owner=id)
    context = {'presentations': presentations}
    return render(request, 'presentations/presentations.html', context)


@login_required(login_url='login')
def updatePresentation_view(request, id):
    presentations = Presentation.objects.get(id=id)
    form = CreatePresentationForm(request.POST or None, instance=presentations)
    context = {
        'presentation_form': form,
        'btn_value': 'Update'
    }
    if form.is_valid():
        form.save()
        # Presentation.user.add(*[request.user])
        return redirect('/detail_pres/'+str(id))

    return render(request, 'presentations/create_presentation.html', context)


@login_required(login_url='login')
def EvaluatePresentation_view(request, id):
    presentation = Presentation.objects.get(id=id)
    questions = Question.objects.all()
    AnswerFormSet = formset_factory(ReviewForm, extra=questions.count())
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            for question, answer in zip(questions, formset.cleaned_data):
                Answer.objects.create(answer=answer['answer'], question=question, author=request.user,
                                      pres_reviewed=presentation)
            return redirect('/detail_pres/' + str(id))
    else:
        formset = AnswerFormSet()

        question_answer_list = zip(formset, questions)
        context = {'presentation': presentation, 'formset': formset, 'question_answer_list': question_answer_list}

        return render(request, 'presentations/evalute_presentation.html', context)


@login_required(login_url='login')
def deletePresentation_view(request, id):
    presentation = Presentation.objects.get(id=id)
    if request.method == "POST":
        presentation.delete()
        return redirect('presentations')

    return render(request, 'presentations/delete-presentation.html', {'presentation': presentation, })


@login_required(login_url='login')
def PresentationDetail_view(request, id):
    answers = Answer.objects.filter(pres_reviewed=id)
    presentations = Presentation.objects.get(id=id)
    questions = Question.objects.all()
    """ 
    Get the average score from the answer Table
    Filters by current presentation, and do the average for all each answer-question
    """
    data = answers.values('question').annotate(avg_answer=Avg('answer'))
    if (data):
        context = {
            'presentations': presentations,
            'reviews': answers,
            'questions': questions,
            # "data": data,
            'review1': data[0]['avg_answer'],
            'review2': data[1]['avg_answer'],
            'review3': data[2]['avg_answer']
        }
    else:
        context = {
            'presentations': presentations,
            'reviews': answers,
            'questions': questions,
            # # "data": data,
            # 'review1': data[0]['avg_answer'],
            # 'review2': data[1]['avg_answer'],
            # 'review3': data[2]['avg_answer']
        }

    return render(request, 'presentations/presentation_detail.html', context)


@login_required(login_url='login')
def PresentationDasboard_view(request, id):
    current_login = request.user
    presentations = Presentation.objects.get(id=id)
    # # evaluations = Evaluation.objects.get(id=id)
    # reviews = Answer.objects.all()
    # dataA = Answer.objects.filter(presentation=presentations).aggregate(
    #     avr_rev1=Avg('review1'),
    #     avr_rev2=Avg('review2'),
    #     avr_rev3=Avg('review3'),
    #
    # )

    # dataJSON = dumps(dataA)
    context = {
        'presentations': presentations,
        'reviews': 'fake',
        'review1_avg': 'avr_rev1',
        'review2_avg': 'avr_rev2',
        'review3_avg': 'avr_rev3',
        'data': {
            'review1': 'avr_rev1',
            'review2': 'avr_rev2',
            'review3': 'avr_rev3'
        }
    }
    print('##################################### SUM ###########################')
    # print(dataA['avr_rev3'])

    return render(request, 'presentations/presentation_dashboard.html', context)


@login_required(login_url='login')
def create_presentation_views(request):
    if request.method == 'POST':
        form = CreatePresentationForm(request.POST, request.FILES)

        if form.is_valid():
            # handle_uploaded_file(request.FILES["Stage_image"])
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            # Presentation.user.add(*[request.user.id])
            return HttpResponseRedirect('/presentations/'+str(request.user.id))
    else:
        form = CreatePresentationForm()

    return render(request, 'presentations/create_presentation.html', {'presentation_form': form, 'btn_value': 'Create'})


def PresentationSearch(request, id):
    search_term = request.GET.get('search-presentations') or ''
    presentations = Presentation.objects.filter(pres_name__contains=search_term, owner=id)
    print(presentations)
    context = {'presentations': presentations}
    return render(request, 'presentations/presentations.html', context)


""" ######################################################### STAGE

The Function below is use to update stage details. when the user 
click on the stage name it brings them to 
the form and filer to only update the stage that was clicked. 
This is possible because we are passing the PK 
as a parameter to the view function
 ############################################################# END """


@login_required(login_url='login')
def updateStage_view(request, id):
    stage = Stage.objects.get(id=id)
    form = CreateStageForm(request.POST or None, instance=stage)
    if form.is_valid():
        form.save()
        return redirect('stage')

    return render(request, 'stage/create_stage.html', {'add_stageForm': form})


@login_required(login_url='login')
def add_stage_view(request):
    submitted = False
    if request.method == 'POST':
        add_stageForm = CreateStageForm(request.POST, request.FILES)
        if add_stageForm.is_valid():
            # handle_uploaded_file(request.FILES["Stage_image"])
            instance = add_stageForm.save(commit=False)

            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/stage')
    else:
        add_stageForm = CreateStageForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'stage/create_stage.html', {'add_stageForm': add_stageForm, 'submitted': submitted})


@login_required(login_url='login')
def deleteStage_view(request, id):
    stage = Stage.objects.get(id=id)
    if request.method == "POST":
        stage.delete()
        return redirect('stage')
    return render(request, 'stage/delete-confirm.html', {'stage': stage, })


@login_required(login_url='login')
def stageDetail_view(request, id):
    presentations = Presentation.objects.filter(stage=id).order_by('-pres_date')
    # dataA = Reviews.objects.filter(presentation__in=presentations).aggregate(
    #     avr_rev1=Avg('review1'),
    #     avr_rev2=Avg('review2'),
    #     avr_rev3=Avg('review3'),
    #
    # )
    # dataA = Reviews.objects.values(presentations.id).annotate(average = Avg('review1'))
    # print(dataA)
    # print(presentations)

    stage = Stage.objects.get(id=id)
    context = {'stage': stage, 'presentations': presentations}
    return render(request, 'stage/view_stage.html', context)


@login_required(login_url='login')
def stage_view(request):
    stages = Stage.objects.all()
    # presnetations = Presentation.objects.()
    context = {
        'Stages': stages,
        # 'number_of_pre':count_pres
    }
    return render(request, 'stage/stage.html', context)


@login_required(login_url='login')
def presentationApproval_view(request, id):
    presentations = Presentation.objects.get(id=id)
    form = approvalForm(request.POST or None, instance=presentations)
    context = {
        'presentation': presentations,
        'presentation_form': form,
        'btn_value': 'Update'
    }
    if form.is_valid():
        form.save()
        # Presentation.user.add(*[request.user])
        return redirect('stage')
    return render(request, 'stage/wating_approval.html', context)

def StageSearch(request):
    search_term = request.GET.get('search-stages') or ''
    stages = Stage.objects.filter(stage_name__contains=search_term)
    print(stages)

    context = {
        'Stages': stages,

    }
    return render(request, 'stage/stage.html', context)
