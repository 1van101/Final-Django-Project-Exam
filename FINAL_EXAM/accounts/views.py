from django.contrib.auth import get_user_model, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_view
from FINAL_EXAM.accounts.forms import AppUserCreateForm, LoginForm

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    template_name = 'accounts/user-register-page.html'
    model = UserModel
    form_class = AppUserCreateForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()  # Save the user to the database
        login(self.request, user)  # Log in the user
        return response


class UserLoginView(auth_view.LoginView):
    template_name = 'accounts/user-login-page.html'
    form_class = LoginForm
    reverse_lazy = reverse_lazy('home page')


class UserLogoutView(auth_view.LogoutView):
    # next_page = reverse_lazy('login user')
    pass


class UserDetailsView(views.CreateView):
    pass


class UserEditView(views.CreateView):
    pass


class UserDeleteView(views.CreateView):
    pass
