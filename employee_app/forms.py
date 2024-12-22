from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile_no', 'gender', 'designation', 'course', 'image']
        widgets = {
            'gender': forms.Select(choices=Employee.gender),
            'designation': forms.Select(choices=Employee.designation),
            'course': forms.Select(choices=Employee.course),
        }





