from django.core.validators import MinValueValidator
from django.db import models


class Recipe(models.Model):
    """
    Recipe model for managing recipe data
    Ingredient field syntax:
    {
        "ingredients": [
            { "name" : "ingredient_name",
              "quantity" : ingredient_quantity
            }
        ]
    }
    Instructions field syntax:
    {
        "instructions": [
            "Instruction 1",
            "Instruction 2"
        ]
    }
    """
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/images/recipe', null=True, blank=True)
    portion = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    ingredients = models.JSONField()
    instructions = models.JSONField()

    def __str__(self):
        return self.title

    def calculate_ingredients(self, quantity=0):
        """
        :param quantity: int
        :return:  ingredients amount calculated based on quantity provided
        """
        if quantity <= 0:
            quantity = self.portion
        data = self.ingredients.get('ingredients')
        if data:
            for key in range(len(data)):
                data[key]['quantity'] *= quantity
            return {'ingredients': data}
        return None
