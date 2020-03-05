from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Answer
from .models import BookmarkQuestion
from .models import BookmarkAnswer

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(BookmarkQuestion)
admin.site.register(BookmarkAnswer)