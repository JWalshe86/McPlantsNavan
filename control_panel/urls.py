from django.urls import re_path

from newsletters.views import control_newsletter, control_newsletter_list

urlpatterns = [
    re_path(r"^newsletter/", control_newsletter, name="control_newsletter"),
    re_path(
        r"newsletter-list", control_newsletter_list, name="control_newsletter_list"
    ),
]
