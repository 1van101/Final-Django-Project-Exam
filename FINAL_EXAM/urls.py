from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path, include
from django.utils.html import strip_tags

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FINAL_EXAM.common.urls')),
    path('accounts/', include('FINAL_EXAM.accounts.urls')),
    path('drawings/', include('FINAL_EXAM.drawings.urls')),
    path('kids/', include('FINAL_EXAM.kids.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


