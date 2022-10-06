from rest_framework import serializers

from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for handling Recipe Data
    """
    ingredients = serializers.SerializerMethodField()
    portion = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_ingredients(self, obj):
        """
        get ingredient's quantity based on portion provided
        """
        portion = self.context.get('portion')
        if portion and portion.replace(".", "1").isnumeric():
            return obj.calculate_ingredients(float(portion))
        return obj.calculate_ingredients()

    def get_portion(self, obj):
        """
        get appropriate portion for given serializer context
        """
        portion = self.context.get('portion')
        if portion and portion.replace(".", "1").isnumeric() and float(portion) > 0:
            return float(portion)
        return obj.portion
