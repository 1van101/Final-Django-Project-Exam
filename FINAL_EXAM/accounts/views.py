from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import views as auth_view
from FINAL_EXAM.accounts.forms import AppUserCreateForm, LoginForm, AppUserEditForm, FilterKidsForm
from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    template_name = 'accounts/user-register-page.html'
    model = UserModel
    form_class = AppUserCreateForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class UserLoginView(auth_view.LoginView):
    template_name = 'accounts/user-login-page.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.request.user.pk})


class UserLogoutView(auth_view.LogoutView):
    pass


@method_decorator(login_required, name='dispatch')
class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_owner = self.request.user == self.object
        user_kids = Kid.objects.all().filter(user_id=self.object.id)
        all_drawings = Drawing.objects.filter(user_id=self.object.id)

        filter_form = FilterKidsForm(user=self.object, data=self.request.GET)
        if filter_form.is_valid():
            filter_by_kid_name_id = filter_form.cleaned_data['filter_by_kid_name']

            # Check if a selection was made before filtering drawings
            if filter_by_kid_name_id:
                filtered_kid = user_kids.get(id=filter_by_kid_name_id)
                all_drawings = Drawing.objects.filter(kid_owner_drawing=filtered_kid)

        context.update({
            'is_owner': is_owner,
            'user_kids': user_kids,
            'form': filter_form,
            'all_drawings': all_drawings
        })
        return context


@method_decorator(login_required, name='dispatch')
class UserEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit-page.html'
    form_class = AppUserEditForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class UserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/user-delete-page.html'
    success_url = reverse_lazy('home page')
