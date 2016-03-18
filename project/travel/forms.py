# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from datetime import datetime, time
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm as DefaultPasswordResetForm, SetPasswordForm as DefaultSetPasswordForm
from allauth.account.forms import SignupForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, Div


def item_pubdate(self, item):
    return datetime.combine(item.posted, time())


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        # Note - include all *required* CustomUser fields here,
        # but don't need to include password1 and password2 as they are
        # already included since they are defined above.
        fields = ("email",)


class ProfileChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ProfileChangePasswordForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            field.label = ''

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/password/change/'
        self.helper.layout = Layout(
            Div(
                Field('new_password1'),
                css_class='col-lg-6'
            ),
            Div(
                Field('new_password2'),
                css_class='col-lg-6'
            ),
            Div(
                Field('old_password'),
                css_class='col-lg-6'
            ),
            Div(
                Submit('save', 'Изменить пароль', css_class='col-lg-12 col-xs-12'),
                css_class='col-lg-6 col-md-12 col-xs-12 col-sm-12'
            ),
        )


class RegistrationForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = _("Username")
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = _("E-mail")
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = _("Password")
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = _("Password (again)")

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/signup/'

        self.helper.layout = Layout(
            Field('username'),
            Field('email'),
            Field('password1'),
            Field('password2'),
            Div(
                Submit('submit', 'Регистрация', css_class='btn btn-blue col-lg-12 col-md-12 col-xs-12 col-sm-12'),
                css_class='form-group'
            ),
        )


class PasswordResetForm(DefaultPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Field('email'),
            Div(
                Submit('submit', 'Изменить пароль', css_class='btn btn-blue col-lg-12 col-md-12 col-xs-12 col-sm-12'),
                css_class='form-group'
            ),
        )


class SetPasswordForm(DefaultSetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Field('new_password1'),
            Field('new_password2'),
            Div(
                Submit('submit', 'Изменить пароль', css_class='btn btn-blue col-lg-12 col-md-12 col-xs-12 col-sm-12'),
                css_class='form-group'
            ),
        )
