from rest_framework import serializers
from .models import Question, Answer, QuestionBookmark, AnswerBookmark
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username'
        )

class AnswerSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)  

    class Meta:
        model = Answer
        fields = (
            'id',
            # 'user'
            'answer_title', 
            'answer_text', 
            'pub_date',
            'question_id'
        )

class QuestionSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)  
    answers = AnswerSerializer(source='answer_set', many=True, required=False)

    class Meta:
        model = Question
        fields = (
            'id',
            # 'user',
            'question_title',
            'question_text',
            'pub_date',
            'answers'
        )
        
class QuestionBookmarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)  
    question = QuestionSerializer(many=False)

    class Meta:
        model = QuestionBookmark
        fields = (
            'id',
            'user',
            'question'
        )

class AnswerBookmarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)  
    answer = AnswerSerializer(many=False)

    class Meta:
        model = AnswerBookmark
        fields = (
            'id',
            'user',
            'answer'
        )
