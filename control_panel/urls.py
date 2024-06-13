from django.urls import re_path

from newsletters.views import control_newsletter

urlpatterns = [
    re_path(r"^newsletter/", control_newsletter, name="control_newsletter"),
]
