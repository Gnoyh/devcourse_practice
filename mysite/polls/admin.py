from django.contrib import admin
from .models import *

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question', 'choice__choice_text']

admin.site.register(Question, QuestionAdmin)