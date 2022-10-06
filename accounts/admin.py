from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class NutritionistAdmin(UserAdmin):
    """
    Customized User admin for Nutritionists
    """
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Nutritionist Data", {"fields": ("recipes", "user_type")}),
    )


class CustomerAdmin(UserAdmin):
    """
    Customized User admin for Customers
    """
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Customer Data", {"fields": ("custom_recipes", "user_type")}),
    )


# Register Nutritionists and Nutritionists to admin panel
admin.site.register(Nutritionist, NutritionistAdmin)
admin.site.register(Customer, CustomerAdmin)
