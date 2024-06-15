from django.urls import re_path

from newsletters.views import (
    control_newsletter,
    control_newsletter_list,
    control_newsletter_detail,
)

urlpatterns = [
    re_path(r"^newsletter/$", control_newsletter, name="control_newsletter"),
    re_path(
        r"^newsletter-list/$", control_newsletter_list, name="control_newsletter_list"
    ),
    re_path(
        r"^newsletter-detail/(?P<pk>\d+)/$",
        control_newsletter_detail,
        name="control_newsletter_detail",
    ),
]
