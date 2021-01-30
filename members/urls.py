from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (SignUpView, EditProfileSuccessView, UserEditView,
                    ChangePasswordView, ChangePasswordSuccessView, ShowProfileView)


app_name = "members"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("user/<int:pk>/edit/", UserEditView.as_view(), name="edit"),
    path("password/", ChangePasswordView.as_view(), name="change_password"),
    path("password_success/", ChangePasswordSuccessView.as_view(),
         name="change_password_success"),
    path("edit_profile_success/",
         EditProfileSuccessView.as_view(), name="edit_success"),
    path("user/<int:pk>/",
         ShowProfileView.as_view(), name="profile"),
]
