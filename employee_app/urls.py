from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name = "register"),
    path('branch_list/',views.branch_list, name = "branch_list"),
    path('salary/',views.salary, name = "salary"),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_edit/', views.employee_edit, name='employee_edit'),
    path('employee_edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('employee_add/', views.employee_add, name='employee_add'),
    path('roles/',views.roles, name = 'roles'),
    path('users/',views.users, name = 'users'),
    path('employees/', views.employees, name='employee_list'),
    path('employee_delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
