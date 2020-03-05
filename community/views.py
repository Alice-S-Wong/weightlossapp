from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import generics

from .models import Question, Answer, QuestionBookmark, AnswerBookmark
from .serializers import QuestionSerializer, AnswerSerializer, QuestionBookmarkSerializer, AnswerBookmarkSerializer

class IndexView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
