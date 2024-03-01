from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [
    path('' , views.main, name='main'),
    path('register-user', views.register_user, name='register_user'),
    path('sign-user/', views.sign_user, name='sign_user'),
    path('create-quiz', views.create_quiz, name='create_quiz'),
]
