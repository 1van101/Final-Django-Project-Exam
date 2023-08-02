from django.urls import path

from FINAL_EXAM.common.views import show_home_page

urlpatterns = (
    path('', show_home_page, name='home page'),

)