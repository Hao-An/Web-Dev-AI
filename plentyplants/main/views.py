from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Article, Comment
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]


def home(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "home.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", {"article": article})


def comment_list(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "comment_list.html", {"article": article})


@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(article=article, author=request.user, content=content)
    return comment_list(request, pk)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_detail", pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, "article_form.html", {"form": form})


# Create your views here.
