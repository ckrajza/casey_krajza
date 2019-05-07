#import path from django
from django.urls import path

#importing views from polls
from . import views

app_name = 'polls'

#adding url patterns
urlpatterns = [
    #index 
    path('', views.IndexView.as_view(), name='index'),
    #polls with question id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #polls with question results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #polls with question votes
    path('<int:question_id>/vote/', views.vote, name='vote'), 
]
