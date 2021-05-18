from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from .models import Article
from . import models
from .models import Question, Choice, Song

from django.http import Http404
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'meditation/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        return {
            'songs': Song.objects.all()
        }


class DetailView(generic.DetailView):
    model = Question
    template_name = 'meditation/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'meditation/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'meditation/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('meditation:results', args=(question.id,)))
