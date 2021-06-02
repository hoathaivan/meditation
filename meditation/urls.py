from django.contrib import admin
from django.urls import path
from . import views

app_name = 'meditation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post, name='post'),

    # CRUD path
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),

    # Email
    path('send_email/', views.send_email, name='send_email')

    # reduant path

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
