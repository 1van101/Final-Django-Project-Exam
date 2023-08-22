from django.urls import path, include

from FINAL_EXAM.drawings.views import AddDrawingView, DetailsDrawingView, DeleteDrawingView, EditDrawingView

urlpatterns = (
    path('add/', AddDrawingView.as_view(), name='add drawing'),
    path('<int:pk>/', include([
        path('', DetailsDrawingView.as_view(), name='details drawing'),
        path('edit/', EditDrawingView.as_view(), name='edit drawing'),
        path('delete/', DeleteDrawingView.as_view(), name='delete drawing'),
    ])
         ),

)
