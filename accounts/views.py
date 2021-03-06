from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout


# Create your views here.

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('workouts:index')
    template_name = 'accounts/login.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.Creatview):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
