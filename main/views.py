from django.shortcuts import render , redirect
from . import models



def index(request):
    context = {}
    return render(request,'base.html',context)


def create_quiz(request):
    if request.method == 'POST':
        models.Quiz.objects.create(
            title = request.POST['name'],
            author = request.POST['author']
        )
    return render(request,)


def list_quiz(request):
    quiz = models.Quiz.object.all()
    context = {"quiz":quiz}
    return render (request, 'base.html', context)