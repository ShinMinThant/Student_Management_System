from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'student_id',
            'email',
            'phone',
            'major',
            'year',
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError(
                'Name is required.'
            )

        if len(name) < 2:
            raise forms.ValidationError(
                'Name must be at least 2 characters.'
            )

        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError(
                'Email is required.'
            )

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            raise forms.ValidationError(
                'Phone number is required.'
            )

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) < 9 or len(phone) > 15:
            raise forms.ValidationError(
                'Phone number must be between 9 and 15 digits.'
            )

        return phone