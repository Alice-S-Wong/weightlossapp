from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import viewsets

from .models import Question, Answer, QuestionBookmark, AnswerBookmark
from .serializers import QuestionSerializer, AnswerSerializer, QuestionBookmarkSerializer, AnswerBookmarkSerializer, UserSerializer
from django.contrib.auth.models import User

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer