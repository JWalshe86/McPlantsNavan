from django.contrib import messages
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(
                request,
                "Your Email Already exists in our database",
                "alert alert-warning alert-dismissible",
            )
        else:
            instance.save()
            messages.success(
                request,
                "Your email has been submitted to the database",
                "alert alert-success alert-dismissible",
            )
            subject = "Thank You For Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Welcome to McPlantsNavan's Online Newsletter. If you would
            like to unsubscribe visit http://127.0.0.1:8000/newsletter/unsubscribe"""
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=signup_message,
                fail_silently=False,
            )
    context = {
        "form": form,
    }
    template = "newsletters/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(
                request,
                "Your email has been removed",
                "alert alert-success alert-dismissible",
            )
            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Sorry to see you go
            please let us know if there was an issue"""
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=signup_message,
                fail_silently=False,
            )
        else:
            messages.warning(
                request,
                "Your email in the database",
                "alert alert-warning alert-dismissible",
            )

    context = {
        "form": form,
    }
    template = "newsletters/unsubscribe.html"
    return render(request, template, context)
