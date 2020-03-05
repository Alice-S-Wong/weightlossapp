from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Answer
from .models import QuestionBookmark
from .models import AnswerBookmark

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionBookmark)
admin.site.register(AnswerBookmark)