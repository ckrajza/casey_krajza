from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone 

from .models import Choice, Question 
# Create your views here.

#Index View class
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #get query set method
    def get_queryset(self):
        """returns last five published questions"""
        return Question.objects.filter(pub_date=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html' 

    

#vote method, takes request and question id
def vote(request, question_id):
    question = get_ibject_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplays the voting form
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,))) 

