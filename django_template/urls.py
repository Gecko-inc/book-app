from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import sync.views
from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="""Simple API for mobile application\nhttps://t.me/nicstim""",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('', include('section.urls')),
    path('', include('account.urls')),
]

urlpatterns += i18n_patterns(

    path('api/', include((api_patterns, 'API'), namespace='api')),

    prefix_default_language=settings.I18N_PREFIX_DEFAULT_LANGUAGE
)

urlpatterns += [
        path('api/', RedirectView.as_view(url='/swagger/', permanent=True)),
        path('', RedirectView.as_view(url='/docs/', permanent=True)),
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
