from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from FINAL_EXAM.common.forms import CommentForm
from FINAL_EXAM.common.models import Like
from FINAL_EXAM.drawings.forms import DrawingForm
from FINAL_EXAM.drawings.models import Drawing

UserModel = get_user_model()


class AddDrawingView(LoginRequiredMixin, views.FormView):
    template_name = 'drawings/drawing-add-page.html'
    form_class = DrawingForm
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = UserModel.objects.get(pk=self.request.user.pk)
        return kwargs

    def form_valid(self, form):
        drawing = form.save(commit=False)
        drawing.user = UserModel.objects.get(pk=self.request.user.pk)
        drawing.save()
        return super().form_valid(form)


class DetailsDrawingView(LoginRequiredMixin, views.DetailView):
    template_name = 'drawings/drawings-detail-page.html'
    model = Drawing
    comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = UserModel.objects.get(pk=self.request.user.pk)
        liked_drawings_by_user = [l.to_drawing_id for l in
                                  user.like_set.all()] if self.request.user.is_authenticated else []
        comments = self.object.comment_set.all()
        likes = self.object.like_set.all()
        likes_list = [l.user.full_name for l in likes]
        is_owner = self.object.user_id == user.id

        context['comment_form'] = self.comment_form
        context['comments'] = comments
        context['likes'] = likes
        context['is_owner'] = is_owner
        context['liked_drawings_by_user'] = liked_drawings_by_user
        context['likes_list'] = likes_list
        return context


class DeleteDrawingView(LoginRequiredMixin, views.DeleteView):
    template_name = 'drawings/drawing-delete-page.html'
    model = Drawing

    success_url = reverse_lazy('home page')
