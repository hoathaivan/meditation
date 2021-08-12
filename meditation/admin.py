from django.contrib import admin

# Register your models here.
from . import models
from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_num')


class BreathAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_num')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Song)
admin.site.register(Sound)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Breath, BreathAdmin)
