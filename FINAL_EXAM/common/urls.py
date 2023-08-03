from django.urls import path

from FINAL_EXAM.common.views import show_home_page, like_functionality

urlpatterns = (
    path('', show_home_page, name='home page'),
    path('like/<int:drawing_id>/', like_functionality, name='like functionality'),

)