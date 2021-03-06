import datetime

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView

from user_profile.models import User, Logger, EditFormIpLogger, ModelSaveSignal
from user_profile.forms import CustomUserChangeForm, SignUpForm

from helpers.get_ip import get_ip


# 1.Add front page, where you'll show your profile data
class MyProfileView(TemplateView):
    template_name = 'my_profile.html'


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


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
    def form_valid(self, form):
        ip = get_ip(self.request)
        EditFormIpLogger.objects.create(
            user_ip=ip,
            user_id=self.request.user.id
        )
        return super().form_valid(form)


class MiddlwareRecords(ListView):
    model = Logger
    template_name = 'logger_list.html'
    paginate_by = 10


class ModelSaveSignalList(ListView):
    model = ModelSaveSignal
    template_name = 'signals_list.html'
    paginate_by = 10


class EditorsIpList(ListView):
    model = EditFormIpLogger
    template_name = 'editors_ip_list.html'
    paginate_by = 10
