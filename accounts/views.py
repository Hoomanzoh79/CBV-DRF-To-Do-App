from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"