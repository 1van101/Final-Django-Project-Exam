from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.forms import AddKidForm
from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()
class AddKidView(views.CreateView):
    form_class = AddKidForm
    template_name = 'kids/kid-add-page.html'
    success_url = reverse_lazy('details profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'user': self.request.user})
        return context

    def form_valid(self, form):
        kid = form.save(commit=False)
        kid.user_id = self.request.user.pk
        kid.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.request.user.pk})


class DetailsKidView(views.DetailView):
    template_name = 'kids/kids-details-page.html'
    model = Kid
    drawings = Drawing.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kid_drawings = self.drawings.filter(kid_owner_drawing_id=self.object.id)
        context['kid_drawings'] = kid_drawings
        return context




class EditKidView(views.UpdateView):
    pass


class DeleteKidView(views.DeleteView):
    pass
