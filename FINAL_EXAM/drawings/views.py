from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from FINAL_EXAM.drawings.forms import DrawingForm

UserModel = get_user_model()


@method_decorator(login_required, name='dispatch')
class AddDrawingView(views.FormView):
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
