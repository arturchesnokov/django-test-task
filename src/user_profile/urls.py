from django.urls import path
from user_profile.views import MyProfileView, EditProfile, MiddlwareRecords

app_name = 'user_profile'

urlpatterns = [
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>', EditProfile.as_view(), name='edit-profile'),
    path('requests-history', MiddlwareRecords.as_view(), name='requests-history'),

]
