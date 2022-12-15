import json
from datetime import time, date
import requests
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.db.models import Sum, Avg
from .forms import *
from .models import *
from django.http import HttpResponseRedirect


@login_required(login_url='login')
def index(request):
    today = date.today()

    presentations = Presentation.objects.filter(owner=request.user, pres_date__gt=today).order_by('pres_date')[:5]
    presentationss = Presentation.objects.filter(owner=request.user, )[:1]
    comments = OpenEndedAnswer.objects.all().filter(pres_reviewed=presentationss, created_at__lte=today).order_by(
        'created_at')[:10]
    context = {
        'presentations': presentations,
        'comments': comments
    }
    return render(request, 'main/index.html', context)


""" ################################################
                    Presentations Views
    ##############################################
"""


@login_required(login_url='login')
def presentation_views(request, id):
    presentations = Presentation.objects.filter(owner=request.user)
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
        return redirect('/detail_pres/' + str(id))

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
            return redirect('/evaluate_pres2/' + str(id))
    else:
        formset = AnswerFormSet()

        question_answer_list = zip(formset, questions)
        context = {'presentation': presentation, 'formset': formset, 'question_answer_list': question_answer_list}
        return render(request, 'presentations/evalute_presentation.html', context)


@login_required(login_url='login')
def OpendEndedEvaluation_view(request, id):
    presentation = Presentation.objects.get(id=id)
    openEndedQuestion = OpenEndedQuestion.objects.all()

    openEnedAnswerFormSet = formset_factory(OpenEndedForm, extra=openEndedQuestion.count())

    if request.method == 'POST':
        formset = openEnedAnswerFormSet(request.POST)
        if formset.is_valid():
            for openQuestion, opneAnswer in zip(openEndedQuestion, formset.cleaned_data):
                OpenEndedAnswer.objects.create(openEndedAnswer=opneAnswer['openEndedAnswer'], question=openQuestion,
                                               author=request.user,
                                               pres_reviewed=presentation)
            return redirect('/detail_pres/' + str(id))
    else:
        formset = openEnedAnswerFormSet()
        question_answer_list = zip(formset, openEndedQuestion)
        context = {'presentation': presentation, 'formset': formset, 'question_answer_list': question_answer_list}

        return render(request, 'presentations/evalute_presentation2.html', context)


@login_required(login_url='login')
def deletePresentation_view(request, id):
    presentation = Presentation.objects.get(id=id)
    if request.method == "POST":
        presentation.delete()
        return redirect('/presentations/'+ str((request.user.id)))

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
    comment = OpenEndedAnswer.objects.filter(pres_reviewed=id)
    print(data)

    if (data):
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27AVG%20Reviews%20Based%20on%20Audience%20Rating%27,data:[" + str(
            data[0]['avg_answer']) + "," + str(data[1]['avg_answer']) + "," + str(
            data[2]['avg_answer']) + "]}]}}&backgroundColor=#012e45"

        context = {
            'OpenEndedAnswer': comment,
            'presentations': presentations,
            'reviews': answers,
            'questions': questions,
            # "data": data,
            'quuickchartURL': url
        }
    else:
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27AVG%20Reviews%20Based%20on%20Audience%20Rating%27,data:[" + str(
            0) + "," + str(0) + "," + str(
            0) + "]}]}}&backgroundColor=#012e45"

        context = {
            'presentations': presentations,
            'reviews': answers,
            'questions': questions,
            'quuickchartURL': url
        }
    return render(request, 'presentations/presentation_detail.html', context)


@login_required(login_url='login')
def create_presentation_views(request):
    if request.method == 'POST':
        form = CreatePresentationForm(request.POST, request.FILES)

        if form.is_valid():
            # handle_uploaded_file(request.FILES["Stage_image"])
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/presentations/' + str((request.user.id)))
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
    stage = Stage.objects.get(id=id)

    # Calculate the average rate, grouped by presentation_id
    # select  presentation_id, avg(rate)
    #   from aba_app_bestpresentation
    #   group by presentation_id
    #   order by rate desc
    #   limit 5;
    best = BestPresentation.objects.filter(stage=id).values('presentation').annotate(avg_answer=Avg('rate'))

    top_presentations = best.order_by('-avg_answer')[:3]

    if len(top_presentations) ==3:
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27TOP%203%20Best%20Presentations%27,data:[" + str(
            top_presentations[0]['avg_answer']) + "," + str(int(top_presentations[1]['avg_answer'])) + "," + str(
            int(top_presentations[2]['avg_answer'])) + "]}]}}&backgroundColor=#012e45"

        print(url)
    elif len(top_presentations) ==2:
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27TOP%203%20Best%20Presentations%27,data:[" + str(
            int(top_presentations[0]['avg_answer'])) + "," + str(int(top_presentations[1]['avg_answer'])) + ",]}]}}&backgroundColor=#012e45"
        print(url)
    elif len(top_presentations) == 1:
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27TOP%203%20Best%20Presentations%27,data:[" + str(
            top_presentations[0]['avg_answer']) + ",]}]}}&backgroundColor=#012e45"
        print(url)
    else:
        url = "https://quickchart.io/chart?c={type:%27bar%27,data:{labels:[1,2,3],datasets:[{label:%27TOP%203%20Best%20Presentations%27,data:[" + str(
            0) + "," + str(0) + "," + str(
            0) + "]}]}}&backgroundColor=#012e45"


    print(presentations)



    """ Takes care of the form """
    if request.method == 'POST':
        form = BestPresentationForm(request.POST, )
        if form.is_valid():
            # handle_uploaded_file(request.FILES["Stage_image"])
            instance = form.save(commit=False)
            instance.author = request.user
            instance.stage = stage
            instance.save()
            return HttpResponseRedirect('/detail_stage/' + str(id))
    else:
        form = BestPresentationForm

    context = {
        'stage': stage,
        'presentations': presentations,
        'form': form,
        'url':url,
        'top_presentations':top_presentations
    }
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
