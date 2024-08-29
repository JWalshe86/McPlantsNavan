from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from .views import handler404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("plants/", include("plants.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("profiles/", include("profiles.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "newsletter/",
        include(
            ("newsletters.urls", "newsletters"),
            namespace="newsletter",
        ),
    ),
    path(
        "control/",
        include(
            ("control_panel.urls", "control_panel"),
            namespace="control_panel",
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "core.views.handler404"

