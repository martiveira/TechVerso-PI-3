from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views
from vagas import views as vagas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('vagas/', include('vagas.urls')),
    path('cursos/', include('cursos.urls')),
    path('sobre/', include('sobre.urls')),
    path("faq/", include("faq.urls")),]
    

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
