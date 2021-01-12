from django.urls import path
from .views import SignUpView # LogInView,

app_name = "members"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
