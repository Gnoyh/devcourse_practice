from django.test import TestCase
from polls_api.serializers import *

# Create your tests here.

class QuestionSerializerTestCase(TestCase):
    def test_with_vaild_data(self):
        serializer = QuestionSerializer(data={'question': 'abc'})
        self.assertEqual(serializer.is_valid(), True)
        new_question = serializer.save()
        self.assertIsNotNone(new_question.id)

    def test_with_invalid_data(self):
        serializer = QuestionSerializer(data={'question': ''})
        self.assertEqual(serializer.is_valid(), False)