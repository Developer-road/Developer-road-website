from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser


class BlogUserAdmin(UserAdmin):
    """
    Defines the display in the admin page
    """

    ordering = ("email",)

    list_display = ("email", "first_name", "last_name",
                    "date_joined", "is_admin")
    search_fields = ("email", "first_name", "last_name",
                     "date_joined", "last_login")

    readonly_fields = ("id", "date_joined", "last_login", "password")

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(BlogUser, BlogUserAdmin)
