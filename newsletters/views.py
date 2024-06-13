from django.contrib import messages
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template


from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm


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
            with open(
                settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt"
            ) as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email,
            )
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
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
            with open(
                settings.BASE_DIR + "/templates/newsletters/unsubscribe_email.txt"
            ) as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email,
            )
            html_template = get_template("newsletters/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
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


def control_newsletter(request):
    form = NewsletterCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == "Publish":
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(
                    subject=subject,
                    from_email=from_email,
                    recipient_list=[email],
                    message=body,
                    fail_silently=True,
                )

    context = {
        "form": form,
    }
    template = "control_panel/control_newsletter.html"
    return render(request, template, context)
