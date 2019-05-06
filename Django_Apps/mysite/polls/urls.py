#import path from django
from django.urls import path

#importing views from polls
from . import views

app_name = 'polls'

#adding url patterns
urlpatterns = [
    #index 
    path('', views.index, name='index'),
    #polls with question id
    path('<int:question_id>/', views.detail, name='detail'),
    #polls with question results
    path('<int:question_id>/results/', views.results, name='results'),
    #polls with question votes
    path('<int:question_id>/vote/', views.vote, name='vote'), 
]
