import logging
from allauth.account.views import LoginView, SignupView, LogoutView
from django.shortcuts import redirect
from django.views.generic import TemplateView

logger = logging.getLogger('user_signin')


class IndexView(TemplateView):
    template_name = 'base.html'


class CustomLoginView(LoginView):
    def form_valid(self, form):
        username = form.cleaned_data.get('login')
        response = super().form_valid(form)
        logger.info(f"User '{username}' signed in successfully.")
        return response

    def form_invalid(self, form):
        username = form.cleaned_data.get('login', 'Unknown User')
        logger.error(f"Failed sign-in attempt for user '{username}'.")
        return super().form_invalid(form)


class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        logger.info(f"User '{self.request.user.username}' signed up successfully.")
        return response


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        logger.warning(f"User '{self.request.user.username}' logged out.")
        return response