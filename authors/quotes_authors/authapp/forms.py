from django.forms import (
    ModelForm,
    CharField,
    TextInput,
    DateField,
)
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=TextInput())
    born_location = CharField(min_length=3, required=True, widget=TextInput())
    description = CharField(min_length=3, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, required=True, widget=TextInput())
    tags = CharField(min_length=3, required=False, widget=TextInput())

    class Meta:
        model = Quote
        fields = ["quote", "author", "tags"]
