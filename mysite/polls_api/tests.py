from django.test import TestCase
from polls_api.serializers import *
from django.contrib.auth.models import User
from polls.models import *

# Create your tests here.
class VoteSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.question = Question.objects.create(
            question = 'test',
            owner = self.user,
        )
        self.choice = Choice.objects.create(
            question = self.question,
            choice_text = '1',
        )

    def test_vote_serializer(self):
        data = {
            'question': self.question.id,
            'choice': self.choice.id,
            'voter': self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        vote = serializer.save()

        self.assertEqual(vote.question, self.question)
        self.assertEqual(vote.choice, self.choice)
        self.assertEqual(vote.voter, self.user)

    def test_vote_serializer_with_duplicate_vote(self):
        choice2 = Choice.objects.create(
            question = self.question,
            choice_text = '2',
        )
        Vote.objects.create(question=self.question, choice=self.choice, voter=self.user)
        
        data = {
            'question': self.question.id,
            'choice': choice2.id,
            'voter': self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_vote_serilaizer_with_unmatched_question_and_choice(self):
        question2 = Question.objects.create(
            question = 'test2',
            owner = self.user,
        )
    
        choice2 = Choice.objects.create(
            question = question2,
            choice_text = '2',
        )
        data = {
            'question': question2.id,
            'choice': choice2.id,
            'voter': self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class QuestionSerializerTest(TestCase):
    def test_with_vaild_data(self):
        serializer = QuestionSerializer(data={'question': 'test'})
        self.assertEqual(serializer.is_valid(), True)
        new_question = serializer.save()
        self.assertIsNotNone(new_question.id)

    def test_with_invalid_data(self):
        serializer = QuestionSerializer(data={'question': ''})
        self.assertEqual(serializer.is_valid(), False)