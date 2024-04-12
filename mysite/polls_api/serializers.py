from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from polls.models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class VoteSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['choice'].question.id != attrs['question'].id:
            raise serializers.ValidationError("Question에 맞는 Choice가 아닙니다.")

        return attrs

    class Meta:
        model = Vote
        fields = ['id', 'question', 'choice', 'voter']
        validators = [
            UniqueTogetherValidator(
                queryset = Vote.objects.all(),
                fields = ['question', 'voter']
            )
        ]

class ChoiceSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['choice_text', 'votes_count']

    def get_votes_count(self, obj):
        return obj.vote_set.count()

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'pub_date', 'owner', 'choices']

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='question-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '두 패스워드가 일치하지 않습니다'})
        
        return attrs

    def create(self, validate_data):
        user = User.objects.create(username=validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}