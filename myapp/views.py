from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import *
from .forms import *


def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'homepage.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to homepage after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})


# Other view functions...

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to homepage or any other desired page after login
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form': form})



# Other view functions...


def user_logout(request):
    logout(request)
    # Redirect to homepage or any other desired page after logout
    return redirect('homepage')


def submit_comment(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article_id
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

