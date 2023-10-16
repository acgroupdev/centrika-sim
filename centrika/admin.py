from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

from .models import Transaction  # Import the Transaction model from your models.py

admin.site.register(Transaction)  # Register the Transaction model


# Define a custom admin class by extending AdminSite
class CustomAdminSite(AdminSite):
    # Set the site title and header
    site_title = _("Custom Admin Dashboard")
    site_header = _("Custom Admin Dashboard")


# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name="custom_admin")

# Register your models with the custom admin site
from .models import Transaction

custom_admin_site.register(Transaction)

# Optionally, you can customize the admin index page
from django.urls import path
from django.http import HttpResponse


def custom_admin_index(request):
    # Custom admin index view
    return HttpResponse("<h1>Welcome to the Custom Admin Dashboard</h1>")


custom_admin_site.index = custom_admin_index

# You can also customize the app list view
custom_admin_site.app_index = custom_admin_index
