from django.urls import path
from . import views


urlpatterns = [
    # token login and logout
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.DiscardAuthToken.as_view(), name="token-logout"),
]