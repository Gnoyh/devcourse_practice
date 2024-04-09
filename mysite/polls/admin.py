from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)