from django.urls import path
from user_profile.views import MyProfileView, EditProfile, MiddlwareRecords, SignUpView, ModelSaveSignalList, \
    EditorsIpList

app_name = 'user_profile'

urlpatterns = [
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit-profile/<int:pk>', EditProfile.as_view(), name='edit-profile'),
    path('requests-history', MiddlwareRecords.as_view(), name='requests-history'),
    path('signals-history', ModelSaveSignalList.as_view(), name='signals-history'),
    path('editors-ip-history', EditorsIpList.as_view(), name='editors-ip-history'),
]
