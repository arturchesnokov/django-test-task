import datetime

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView

from user_profile.models import User, Logger, EditFormIpLogger
from user_profile.forms import CustomUserChangeForm, SignUpForm


# 1.Add front page, where you'll show your profile data
class MyProfileView(TemplateView):
    template_name = 'my_profile.html'


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# 5. Create a page where you may change your profile.
class EditProfile(UpdateView):
    template_name = 'edit_profile.html'
    form_class = CustomUserChangeForm
    queryset = User.objects.filter(is_active=True)
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)

    # * Save IP of user who makes edit.
    def get_success_url(self):
        ip = get_ip(self.request)
        EditFormIpLogger.objects.create(
            user_ip=ip,
            user_id=self.request.user.id
        )

        return super().get_success_url()


class MiddlwareRecords(ListView):
    model = Logger
    template_name = 'logger_list.html'
    paginate_by = 10
