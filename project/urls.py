from django.conf import settings
from django.conf.urls import include, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.static import serve
from django.conf.urls.static import static

admin.autodiscover()

handler400 = 'project.views.e400'
handler403 = 'project.views.e403'
handler404 = 'project.views.e404'

urlpatterns = [
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('seo.urls', namespace='seo')),
    path('forms/', include('forms.urls', namespace='forms')),
    path('', include('about.urls', namespace='about')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('contacts.urls', namespace='contacts')),
    path('', include('events.urls', namespace='events')),
    path('', include('projects.urls', namespace='projects')),
    path('', include('services.urls', namespace='services')),
    path('', include('homepage.urls', namespace='homepage'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if getattr(settings, 'ENV', 'production') == 'dev':
    urlpatterns += (
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    )
    urlpatterns += tuple(staticfiles_urlpatterns())

urlpatterns += (
    path('', include('pages.urls', namespace='pages')),
)
