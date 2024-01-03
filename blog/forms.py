from django import forms
from .models import Contact, Newsletter


class ContactForms(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForms(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"
