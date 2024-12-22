# Employee_management_system/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee_app.urls')),  # Include app URLs without namespace here
]
