from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FINAL_EXAM.common.urls')),
    path('accounts/', include('FINAL_EXAM.accounts.urls')),
    path('drawings/', include('FINAL_EXAM.drawings.urls')),
    path('kids/', include('FINAL_EXAM.kids.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    handler400 = TemplateView.as_view(template_name='400.html')
    handler403 = TemplateView.as_view(template_name='403.html')
    handler500 = TemplateView.as_view(template_name='500.html')
