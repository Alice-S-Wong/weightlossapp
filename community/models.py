from django.db import models

# Create your models here.
from django.conf import settings

class Question(models.Model):
    question_title = models.CharField(max_length=255)
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class Answer(models.Model):
    answer_title = models.CharField(max_length=255)
    answer_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class QuestionBookmark(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class AnswerBookmark(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )