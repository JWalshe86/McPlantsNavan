from django.urls import re_path

from newsletters.views import (
    control_newsletter,
    control_newsletter_list,
    control_newsletter_detail,
    control_newsletter_edit,
    control_newsletter_delete,
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
    re_path(
        r"^newsletter-edit/(?P<pk>\d+)/$",
        control_newsletter_edit,
        name="control_newsletter_edit",
    ),
    re_path(
        r"^newsletter-delete/(?P<pk>\d+)/$",
        control_newsletter_delete,
        name="control_newsletter_delete",
    ),
]
