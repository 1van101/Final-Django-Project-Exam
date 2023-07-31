from django.urls import path

from FINAL_EXAM.drawings.views import AddDrawingView

urlpatterns = (
    path('add/', AddDrawingView.as_view(), name='add drawing'),

)