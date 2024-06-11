from django import forms
from crispy_forms.helper import FormHelper

from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):

    class Meta:
        model = NewsletterUser
        fields = ["email"]

        def clean_email(self):
            email = self.cleaned_data.get("email")

            return email
