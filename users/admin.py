# Users admin.

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms

# Models
from users.models import User

class UserCreationForm(forms.ModelForm):
    """Form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'last_login')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the field does not have access to the initial value
        return self.initial["password"]

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """User admin"""

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['pk', 'username', 'email', 'is_staff', 'is_active', 'created']
    list_display_links = ['pk', 'username']
    list_editable = ['email']
    list_filter = ['created', 'email', 'is_staff', 'is_active']
    search_fields = ['created', 'email', 'username', 'is_staff', 'is_active']
    ordering = ['email']
    
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        (None, {
            'fields': ('password1', 'password2', )
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff')
        }),
        ('Important dates', {
            'fields': ('created', 'updated')
        }),
    )

    readonly_fields = ('created', 'updated')

# Ensure you are importing UserAdmin as well as the required forms and the admin module.
