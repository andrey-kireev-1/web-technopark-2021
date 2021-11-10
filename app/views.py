from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import *

questions = [
    {
        'title': f"Заголовок лучшего вопроса {i}",
        'text': f"Текст лучшего вопроса {i}",
        'id': i
    } for i in range(100)
]

def index(request):
    return render(request, "index.html")

def ask(request):
    return render(request, "ask.html")
    
def settings(request):
    return render(request, "settings.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", { 'questions': content})

def question(request, id):
    return render(request, "question.html")

tag_names = ['perl', 'Python', 'TechnoPark', 'MySQL', 'django', 'Mail.Ru', 'Voloshin', 'Firefox']

questions = [
    {
        'title': f"Заголовок вопроса по тегу {i}",
        'text': f"Текст вопроса по тегу {i}",
        'id': i
    } for i in range(100)
]

def tag(request, name):
    i = 0
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    while(tag_names):
        if tag_names[i] == name:
            context = {'title': name,'questions': content}
            break
        i += 1
    return render(request, "tag.html", context)