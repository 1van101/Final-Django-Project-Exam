from django.urls import path

from FINAL_EXAM.common.views import Index

urlpatterns = (
    path('', Index.as_view(), name='home page'),

)