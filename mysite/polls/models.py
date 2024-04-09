from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    # score = models.FloatField(default=0.0)
    # is_something_wrong = models.BooleanField(default=False)
    # json_field = models.JSONField(default=dict)

    @admin.display(boolean=True, description="최근 생성(하루 기준)")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        if self.was_published_recently():
            new_badge = "(NEW)"
        else:
            new_badge = ""

        return f'{new_badge} 제목: {self.question}, 날짜: {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.question.question}] {self.choice_text}'