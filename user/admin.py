from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'full_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone', 'full_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    search_fields = ('phone',)
    ordering = ('phone',)


admin.site.register(CustomUser, CustomUserAdmin)
