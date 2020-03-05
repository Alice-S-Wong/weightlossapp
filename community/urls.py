from django.urls import path

from . import views


app_name = 'community'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('answers', views.AnswerView.as_view()),
    # path('bookmarks', views.bookmarks, name='bookmarks')
]