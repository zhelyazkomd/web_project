from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from web_project.accounts.forms import SignUpForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'is_staff', ]
    list_filter = ()
    form = UserEditForm
    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", 'password1', 'password2'),
                # TODO: add""password1", "password2","
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "age",),
            },
        ),
    )

    fieldsets = (
        (None,
         {"fields":
              ("email",
               "password"
               )}),

        (
            ("Personal info"
             ),
            {
                "fields":
                    (
                        "date_joined",
                    )}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    # "user_permissions",
                ),
            },
        ),
        (
            ("Important dates"),
            {"fields": (
                "last_login",
            )}),
    )
