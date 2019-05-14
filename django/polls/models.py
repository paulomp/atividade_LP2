from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=280)
    date_pub = models.DateTimeField('publication date')

class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

