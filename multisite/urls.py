from django.conf import settings
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from search import views as search_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('edit/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
]

# http://docs.wagtail.io/en/v2.0/advanced_topics/i18n/
urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning

    path('search/', search_views.search, name='search'),

    # Optional URL for including your own vanilla Django urls/views
    # url(r'', include('myapp.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    path('web/', include(wagtail_urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
