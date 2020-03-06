from rest_framework import serializers
from .models import Question, Answer, QuestionBookmark, AnswerBookmark
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
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
    user_set = UserSerializer(many=False)  
    answers = AnswerSerializer(source='answer_set', many=True, required=False)

    class Meta:
        model = Question
        fields = (
            'id',
            'user_set',
            'question_title',
            'question_text',
            'pub_date',
            'answers'
        )
    
    def create(self, validated_data):
        users = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for user in users:
            User.objects.create(**user, question=question)
        return question
        
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
