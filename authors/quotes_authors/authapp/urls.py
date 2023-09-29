from django.urls import path
from . import views

app_name = "authapp"

urlpatterns = [
    path("", views.main, name="main"),
    path("", views.show_authors, name="authors"),
    path("author/", views.author, name="author"),
    path("quote/", views.quote, name="quote"),
    path("detail/<int:author_id>", views.detail, name="detail"),
    path("delete/<int:quote_id>", views.delete_quote, name="delete"),
    path("deleteauthor/<int:author_id>", views.delete_author, name="deleteauthor"),
    path("load/", views.load_quotes_authors, name="load"),
]
