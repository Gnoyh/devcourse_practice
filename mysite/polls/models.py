from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # score = models.FloatField(default=0.0)
    # is_something_wrong = models.BooleanField(default=False)
    # json_field = models.JSONField(default=dict)

    def __str__(self):
        return f'제목: {self.question}, 날짜: {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)