import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=280)
    date_pub = models.DateTimeField('publication date')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)


class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
