from django.urls import re_path

from .views import newsletter_signup, newsletter_unsubscribe

urlpatterns = [
    re_path(
        r'sign_up/$',
        newsletter_signup,
        name="newsletter_signup"
    ),
    re_path(
        r'unsubscribe/$',
        newsletter_unsubscribe,
        name='newsletter_unsubscribe'
    ),
]
