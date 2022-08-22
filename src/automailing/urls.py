from django.contrib import admin
from django.urls import include, path

from utils.openapi_schema_generator import get_schema_view

admin.autodiscover()

schema_view = get_schema_view(title="Automailing", version="1.0")

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("swagger/", schema_view.with_ui("swagger",
                     cache_timeout=0), name="schema-swagger-ui"),
                path("redoc/", schema_view.with_ui("redoc",
                     cache_timeout=0), name="schema-redoc"),
                path("accounts/", include("modules.mailing.rest.urls")),
            ]
        ),
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
