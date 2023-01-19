from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls

# admin.autodiscover()


# static_urlpatterns = [
#     re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
#     re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
# ]

urlpatterns = [
    # path('', include(static_urlpatterns)),
    path('', include('base.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sys/managment/admin/', admin.site.urls),
    path('posts/', include('post.urls')),
    path('account/', include('account.urls')),
    path('categories/', include('category.urls')),
    path('courses/', include('course.urls')),
    path('bankgateway/', az_bank_gateways_urls()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
