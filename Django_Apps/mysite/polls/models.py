from django.db import models

import datetime
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    #question text with max length of 200 characters
    question_text = models.CharField(max_length=200)
    
    #publish date labelled as "date published"
    pub_date = models.DateTimeField('date published')

    #adding string method
    def __str__(self):
        return self.question_text

    #adding recently published method, checks if question was posted within one day
    def was_published_recently(self):
        now = timezone.now() 
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
    


class Choice(models.Model):
    #question set as foreign key with cascade on delete
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    #choice text, response to question, with max length of 200 characters
    choice_text = models.CharField(max_length=200)

    #votes for each choice, defaulted to 0
    votes = models.IntegerField(default=0)

    #adding string method
    def __str__(self):
        return self.choice_text 
