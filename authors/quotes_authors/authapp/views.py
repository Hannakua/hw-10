from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from django.contrib.auth.decorators import login_required
import json


def main(request):
    quotes = Quote.objects.all()
    authors = Author.objects.all()
    data = {"quotes": quotes, "authors": authors}
    return render(request, "authapp/index.html", context=data)


def show_authors(request):
    authors = Author.objects.all()
    return render(request, "authapp/index.html", {"authors": authors})


@login_required
def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to="authapp:main")
        else:
            return render(
                request,
                "authapp/author.html",
                {"form": form},
            )

    return render(
        request,
        "authapp/author.html",
        {"form": AuthorForm()},
    )


@login_required
def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        authors = Author.objects.all().order_by("fullname")  # Отримати список авторів
        data = {
            "form": form,
            "authors": authors,  # Передати список авторів у контекст
        }
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect(to="authapp:main")
        else:
            return render(
                request,
                "authapp/quote.html",
                data,
            )
    form = QuoteForm()
    authors = Author.objects.all().order_by("fullname")  # Отримати список авторів
    data = {
        "form": form,
        "authors": authors,  # Передати список авторів у контекст
    }
    return render(
        request,
        "authapp/quote.html",
        data,
    )


# @login_required
def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "authapp/detail.html", {"author": author})


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to="authapp:main")


@login_required
def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return redirect(to="authapp:main")


@login_required
def load_quotes_authors(request):
    with open("authors.json", "r", encoding="utf-8") as file_auth:
        authors_db = json.load(file_auth)

    for auth in authors_db:
        Author.objects.create(
            fullname=auth["fullname"],
            born_date=auth["born_date"],
            born_location=auth["born_location"],
            description=auth["description"],
        )

    with open("quotes.json", "r", encoding="utf-8") as file_que:
        quotes_db = json.load(file_que)
        # authors_ = Author.objects.all()

        for quo in quotes_db:
            author, data = Author.objects.get_or_create(fullname=quo["author"])

            Quote.objects.create(quote=quo["quote"], author=author, tags=quo["tags"])

    return redirect(to="authapp:main")

