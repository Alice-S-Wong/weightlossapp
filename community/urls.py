from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('questions', views.QuestionView)
router.register('answers', views.AnswerView)

app_name = 'community'
urlpatterns = [
    path('', include(router.urls)),
    # path('bookmarks', views.bookmarks, name='bookmarks')
]