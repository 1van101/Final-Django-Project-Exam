from django.urls import path, include

from FINAL_EXAM.common.views import show_home_page, like_functionality, AddCommentView

urlpatterns = (
    path('', show_home_page, name='home page'),
    path('like/<int:drawing_id>/', like_functionality, name='like functionality'),
    path('comment/<int:drawing_id>/', AddCommentView.as_view(), name='add comment'),
)
