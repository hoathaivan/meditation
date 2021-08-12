import datetime

from django.db import models
from django.contrib import admin
# Create your models here.
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


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


class Sound(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Breath(models.Model):
    name = models.CharField(max_length=200)
    tool_tip = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='breaths', default='breaths/placeholder.png')
    breath_ratio = models.CharField(max_length=60)
    order_num = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + str(self.order_num)


class Theme(models.Model):
    name = models.CharField(max_length=200)
    tool_tip = models.CharField(max_length=500)
    background = models.ImageField(upload_to='themes', default='themes/placeholder.png')
    thumbnail = models.ImageField(upload_to='themes/thumbnails', default='themes/thumbnails/placeholder.png')
    active = models.BooleanField(default=False)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' ' + str(self.order_num)


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=512, null=True, blank=True)
    note = models.CharField(max_length=1024, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='posts/thumbnails',
                                  default='posts/thumbnails/placeholder.png')
    background = models.ImageField(null=True, blank=True, upload_to='posts/backgrounds',
                                   default='posts/backgrounds/placeholder.png')
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, null=True)

    slug = models.SlugField(null=True, blank=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug is None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)


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
