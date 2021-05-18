import datetime

from django.db import models
from django.contrib import admin
# Create your models here.
from django.utils import timezone


# Meditation app models
class Song(models.Model):
    name = models.CharField(max_length=200)
    artis = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default='thumbnail-player.jpg')
    score = models.IntegerField(default=0)
    length_text = models.CharField(max_length=8)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
