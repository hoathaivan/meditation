import django_filters
from django_filters import CharFilter
from meditation.models import *
from django import forms


class PostFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Tiêu đề')
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple,
                                                    label='Thẻ'
                                                    )

    class Meta:
        model = Post
        fields = ['headline', 'tags']
