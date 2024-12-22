from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'home.html')  # Renders the Home Page

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("Username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login successful. Redirecting to dashboard...")
            return redirect('dashboard')
        else:
            print("Invalid login details")
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')  # Renders the Dashboard Page

from django.shortcuts import redirect

def logout_view(request):
    # Clear the session (or cookies) for logout
    request.session.flush()  # Clears all session data
    return redirect('home')  # Redirect to Home Page
def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
            return redirect('register')

        # Create and save user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Redirect to login with success message
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'register.html')

from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def branch_list(request):
    return render(request, 'branch_list.html')  # Renders the Dashboard Page
def salary(request):
    return render(request, 'salary.html')  # Renders the Dashboard Page
def employees(request):
    return render(request, 'employee_list.html')  # Renders the Dashboard Page

def roles(request):
    return render(request, 'roles.html')

from django.shortcuts import render
from .models import UserRegistration

def users(request):
    users = UserRegistration.objects.all()
    return render(request, 'users.html', {'users': users})
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Employee

def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        try:
            # Update employee fields
            employee.name = request.POST.get('name', employee.name)
            employee.email = request.POST.get('email', employee.email)
            validate_email(employee.email)  # Validate email format
            employee.mobile_no = request.POST.get('mobile_no', employee.mobile_no)
            employee.designation = request.POST.get('designation', employee.designation)
            employee.gender = request.POST.get('gender', employee.gender)
            employee.course = request.POST.get('course', employee.course)  # Direct assignment

            # Update image if uploaded
            if 'image' in request.FILES:
                employee.image = request.FILES['image']

            # Save changes
            employee.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect(reverse('employee_list'))
        except ValidationError as e:
            messages.error(request, f'Error: {e.message}')
        except Exception as e:
            messages.error(request, f'Unexpected error: {str(e)}')

    return render(request, 'employee_edit.html', {'employee': employee})




from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)  # Make sure to handle files with request.FILES
        if form.is_valid():
            form.save()  # Save the form if valid
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')  # Redirect to employee list page
        else:
            messages.error(request, 'There was an error adding the employee. Please check the form.')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})







from django.shortcuts import get_object_or_404, redirect
from .models import Employee

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Password Reset View
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


# Password Reset Done View
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


# Password Reset Confirm View
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


# Password Reset Complete View
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
