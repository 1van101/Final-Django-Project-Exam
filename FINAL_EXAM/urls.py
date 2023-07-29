
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FINAL_EXAM.common.urls')),
    path('accounts/', include('FINAL_EXAM.accounts.urls')),
    path('drawings/', include('FINAL_EXAM.drawings.urls')),
    # path('kids/', include('FINAL_EXAM.kids.urls'))
]
