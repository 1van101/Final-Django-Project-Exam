from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.forms import AddKidForm, KidEditForm
from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()


class AddKidView(LoginRequiredMixin, views.CreateView):
    form_class = AddKidForm
    template_name = 'kids/kid-add-page.html'
    success_url = reverse_lazy('details profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'user': self.request.user})
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_visitor:
            # If user is a visitor redirect them to home page
            return redirect('home page')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        kid = form.save(commit=False)
        kid.user_id = self.request.user.pk
        kid.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.request.user.pk})


class DetailsKidView(LoginRequiredMixin, views.DetailView):
    template_name = 'kids/kid-details-page.html'
    model = Kid
    drawings = Drawing.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kid_drawings = self.drawings.filter(kid_owner_drawing_id=self.object.id)
        is_owner = self.object.user_id == self.request.user.id
        context['kid_drawings'] = kid_drawings
        context['is_owner'] = is_owner

        return context


class EditKidView(LoginRequiredMixin, views.UpdateView):
    template_name = 'kids/kid-edit-page.html'
    model = Kid
    form_class = KidEditForm

    def get_success_url(self):
        user_id = self.object.user_id
        slug = self.object.slug
        return reverse_lazy('details kid', kwargs={'user_id': user_id, 'slug': slug})


class DeleteKidView(LoginRequiredMixin, views.DeleteView):
    template_name = 'kids/kid-delete-page.html'
    model = Kid
    success_url = reverse_lazy('home page')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     delete_action = "{% url 'delete kid' object.user_id object.slug %}"
    #     context['delete_action'] = delete_action
    #     return context
