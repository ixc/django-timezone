"""
Root URLconf for ``timezone.tests`` project.
"""

from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timezone/', include('timezone.urls')),
)
