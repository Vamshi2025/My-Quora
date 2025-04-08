from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer

def redirect_to_login(request):
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'quora_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'quora_app/login.html', {'form': form})

@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'quora_app/home.html', {'questions': questions})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.user = request.user
            q.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'quora_app/ask_question.html', {'form': form})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.question = question
            a.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'quora_app/question_detail.html', {
        'question': question, 'answers': answers, 'form': form
    })

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)
