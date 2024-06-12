from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from django.views.static import serve
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("plants/", include("plants.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("profiles/", include("profiles.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(
        r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATICFILES_DIRS}
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    re_path(
        r"^newsletter/",
        include(
            ("newsletters.urls", "newsletters"),
            namespace="newsletter",
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "core.views.handler404"
