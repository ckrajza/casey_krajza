from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#index method
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list} 
    return render(request, 'polls/index.html', context)

#detail method, takes request and question id
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question}) 

#results method, takes request and question id
def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

#vote method, takes request and question id
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id) 

