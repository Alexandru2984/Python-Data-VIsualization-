from django.urls import path
from .views import choose_countries_view
from .views import all_countries_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

	path("all", all_countries_view),
	path("choose", choose_countries_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)