from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect



class PermissionMixin(auth_mixins.UserPassesTestMixin, auth_mixins.LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('index')