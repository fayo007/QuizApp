from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import xlwt
from django.http import HttpResponse



# exelga generatsiya qilish 

def generate_excel(request):
    queryset = Result.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')

    row_num = 0
    columns = [
        "Field1",
        "Field2",
    ]
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)
    for obj in queryset:
        row_num += 1
        for col_num, column_name in enumerate(columns):
            value = getattr(obj, column_name)
            ws.write(row_num, col_num, value)
    wb.save(response)
    return response



@login_required(login_url = 'dash:register_user')
def main(request):
    quizes = Quiz.objects.filter(author = request.user)
    context = {
        "quizes" : quizes
    }
    return render(request, 'index.html', context)

# quizes

@login_required(login_url = 'dash:register_user')
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST['title']
        Quiz.objects.create(
            title = title,
            author = request.user 
        )
        return render(request,'quiz/create-question.html')
    return render(request,'quiz/create-quiz.html')


# questions

@login_required(login_url = 'dash:login')
def create_question(request, id):
    quiz = Quiz.objects.get(id = id)
    if request.method == 'POST':
        
        title = request.POST['title']
        ques = Question.objects.create(
            quiz = quiz,
            title = title
        )
        Option.objects.create(
            question = ques,
            name = request.POST['correct'],
            is_correct = True
        )
        data = [request.POST['incorrect1'], request.POST['incorrect2'], request.POST['incorrect3']]

        for i in data:
            Option.objects.create(
                question = ques,
                name = i,
            )
        if request.POST['submit_action'] == 'exit':
            return redirect('dash:main')

    return render (request, 'quiz/create-question.html' )
    
# authentication

def register_user(request) :
    if request. method == 'POST':
        username = request. POST ['username']
        password = request. POST ['password']
        User.objects. create_user(
            username = username,
            password=password
        )
        return redirect('dash:main')
    return render (request,'auth/register.html')


def sign_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(username = username, password=password)
        if user:
            login(request, user)
            return redirect('dash:main')
        
    return render(request,'auth/login.html')

