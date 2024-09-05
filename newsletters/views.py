from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm


def newsletter_signup(request):
    """Handle newsletter sign-up form submission."""

    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(
                request,
                "Your email already exists in our database.",
                "alert alert-warning alert-dismissible",
            )
        else:
            instance.save()
            messages.success(
                request,
                "Your email has been submitted to the database.",
                "alert alert-success alert-dismissible",
            )
            subject = "Thank You For Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(
                settings.BASE_DIR / "templates/newsletters/sign_up_email.txt"
            ) as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email,
            )
            html_template = get_template(
                "newsletters/sign_up_email.html"
            ).render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {"form": form}
    template = "newsletters/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    """Handle newsletter unsubscribe form submission."""

    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(
                request,
                "Your email has been removed.",
                "alert alert-success alert-dismissible",
            )
            subject = "You Have Been Unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(
                settings.BASE_DIR
                / "templates/newsletters/unsubscribe_email.txt"
            ) as f:
                unsubscribe_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=unsubscribe_message,
                from_email=from_email,
                to=to_email,
            )
            html_template = get_template(
                "newsletters/unsubscribe_email.html"
            ).render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:
            messages.warning(
                request,
                "Your email is not in the database.",
                "alert alert-warning alert-dismissible",
            )

    context = {"form": form}
    template = "newsletters/unsubscribe.html"
    return render(request, template, context)


@staff_member_required
def control_newsletter(request):
    """Render the newsletter creation form and handle submission."""

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
        return redirect(
            "control_panel:control_newsletter_list"
        )

    context = {"form": form}
    template = "control_panel/control_newsletter.html"
    return render(request, template, context)


def control_newsletter_list(request):
    """Display a paginated list of newsletters."""

    newsletters = Newsletter.objects.all()
    paginator = Paginator(newsletters, 10)
    page = request.GET.get("page")

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        "items": items,
        "page_range": page_range,
    }
    template = "control_panel/control_newsletter_list.html"
    return render(request, template, context)


def control_newsletter_detail(request, pk):
    """Display the details of a specific newsletter."""

    newsletter = get_object_or_404(Newsletter, pk=pk)

    context = {"newsletter": newsletter}
    template = "control_panel/control_newsletter_detail.html"
    return render(request, template, context)


def control_newsletter_edit(request, pk):
    """Edit an existing newsletter."""

    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == "POST":
        form = NewsletterCreationForm(request.POST, instance=newsletter)

        if form.is_valid():
            newsletter = form.save()
            if newsletter.status == "Published":
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
            return redirect(
                "control_panel:control_newsletter_detail", pk=newsletter.pk
            )

    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {"form": form}
    template = "control_panel/control_newsletter.html"
    return render(request, template, context)


def control_newsletter_delete(request, pk):
    """Delete a specific newsletter."""

    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == "POST":
        form = NewsletterCreationForm(request.POST, instance=newsletter)

        if form.is_valid():
            newsletter.delete()
            return redirect(
                "control_panel:control_newsletter_list"
            )

    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {"form": form}
    template = "control_panel/control_newsletter_delete.html"
    return render(request, template, context)
