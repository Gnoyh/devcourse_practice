from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/result/', result, name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('signup/', SignupView.as_view()),
]
