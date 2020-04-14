from django.contrib import admin
from user_profile.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['email',
              'username',
              'is_active',
              'first_name',
              'last_name',
              'date_of_birth',
              'biography',
              'contacts']


admin.site.register(User, UserAdmin)
