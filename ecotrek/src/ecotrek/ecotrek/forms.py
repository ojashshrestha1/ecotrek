from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"Fullname",
				"id":"name"
				}
			)
		)

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"password",
				"id":"password"
				}
			)

		)

class RegisterForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"Fullname",
				"id":"fullname"
				}
			)
		)
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"username",
				"id":"username"
				}
			)
		)

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"password",
				"id":"password"
				}
			)

		)

	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"input-md round form-control",
				"placeholder":"confirm password",
				"id":"confirm-password"
				}
			)

		)
	def clean_username():
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("the username is already taken")
		return username
	def clean(self):
		data = self.cleaned_data.get('password')
		data1 = self.cleaned_data.get('password1')
		if password1 != password:
			print("hellow")
		return data