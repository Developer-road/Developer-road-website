from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, UserEditView, ChangePasswordView, ChangePasswordSuccessView


app_name = "members"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_user/", UserEditView.as_view(), name="edit"),
    path("password/", ChangePasswordView.as_view(), name="change_password"),
    path("password_success/", ChangePasswordSuccessView.as_view(), name="change_password_success"),
]
