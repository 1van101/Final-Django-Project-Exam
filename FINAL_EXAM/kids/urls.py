from django.urls import path, include

from FINAL_EXAM.kids.views import AddKidView, DetailsKidView, EditKidView, DeleteKidView

urlpatterns = (
    path('add/', AddKidView.as_view(), name='add kid'),
    path('<str:user>/kid/<slug:slug>/', include([
        path('', DetailsKidView.as_view(), name='details kid'),
        path('edit/', EditKidView.as_view(), name='edit kid'),
        path('delete/', DeleteKidView.as_view(), name='delete kid'),
    ]))
)

