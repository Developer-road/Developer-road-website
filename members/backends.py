from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CaseModelBackend(ModelBackend):
    """
    Fix the problem of the login with insensitive email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel =  get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_user_name_field = f"{UserModel.USERNAME_FIELD}__iexact"
            user = UserModel._default_manager.get(**{case_insensitive_user_name_field: username})

        except UserModel.DoesNotExist:
            UserModel().set_password(password)

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user