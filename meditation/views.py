from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from .models import Article
from . import models
from .models import *
from django.contrib.auth.decorators import login_required

from django.http import Http404
from django.views import generic
from .forms import PostForm
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


class IndexView(generic.ListView):
    template_name = 'meditation/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        return {
            'posts': Post.objects.filter(active=True, featured=True)[0:3],
            'songs': Song.objects.all(),
            'sounds': Sound.objects.all()
        }


def posts(request):
    posts_db = Post.objects.filter(active=True)
    my_filter = PostFilter(request.GET, queryset=posts_db)
    posts_db = my_filter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts_db, 2)

    try:
        posts_db = paginator.page(page)
    except PageNotAnInteger:
        posts_db = paginator.page(1)
    except EmptyPage:
        posts_db = paginator.page(paginator.num_pages)

    context = {
        'posts': posts_db,
        'my_filter': my_filter
    }
    return render(request, 'meditation/posts.html', context)


def post(request, slug):
    post_db = Post.objects.get(slug=slug)
    context = {
        'post': post_db
    }
    return render(request, 'meditation/post.html', context)


@login_required(login_url='meditation:index')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meditation:posts')

    context = {'form': form}
    return render(request, 'meditation/post_form.html', context)


@login_required(login_url='meditation:index')
def update_post(request, slug):
    post_db = Post.objects.get(slug=slug)
    form = PostForm(instance=post_db)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_db)
        if form.is_valid():
            form.save()
        return redirect('meditation:posts')

    context = {'form': form}
    return render(request, 'meditation/post_form.html', context)


@login_required(login_url='meditation:index')
def delete_post(request, slug):
    post_db = Post.objects.get(slug=slug)
    if request.POST == 'POST':
        post_db.delete()
        return redirect('meditation:posts')
    context = {'item': post_db}
    return render(request, 'meditation/delete_post.html', context)


def send_email(request):
    if request.method == 'POST':
        template = render_to_string('meditation/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['thiendinhonline@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request, 'meditation/email_sent.html')


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
