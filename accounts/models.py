from django.contrib.auth.models import AbstractUser
from django.db import models

from recipe.models import Recipe


class User(AbstractUser):
    """
    Base user model for authentication
    """
    user_types_choices = [('NUTRITIONIST', 'Nutritionist'), ('CUSTOMER', 'Customer')]
    user_type = models.CharField(max_length=25, choices=user_types_choices)

    @property
    def is_nutritionist(self):
        return self.user_type == 'NUTRITIONIST'

    @property
    def is_customer(self):
        return self.user_type == 'CUSTOMER'


class Nutritionist(User):
    """
    Nutritionist model for handling users of type NUTRITIONIST
    """
    recipes = models.ManyToManyField(Recipe, related_name='nutritionist', blank=True)

    class Meta:
        verbose_name = 'Nutritionist'


class Customer(User):
    """
    Customer model for handling users of type CUSTOMER
    """
    custom_recipes = models.ManyToManyField(Recipe, related_name='customer', blank=True)

    class Meta:
        verbose_name = 'Customer'
