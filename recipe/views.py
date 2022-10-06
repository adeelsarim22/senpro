from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class ListRecipe(generics.ListCreateAPIView):
    """
    API View for handling requests related to listing recipes.
    Only recipes created by user ( in case of Nutritionist ) or assigned to user ( in case of Customer )
    are shown.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recipe.objects.filter(nutritionist=self.request.user) | Recipe.objects.filter(
                customer=self.request.user)
        return None


class RetrieveRecipe(generics.RetrieveAPIView):
    """
    API View for handling requests related to Retrieving a particular recipes.
    Only recipes created by user ( in case of Nutritionist ) or assigned to user ( in case of Customer )
    are shown.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recipe.objects.filter(nutritionist=self.request.user) | Recipe.objects.filter(
                customer=self.request.user)
        return None

    def get_serializer_context(self):
        """
        Allow user to get a particular recipe with a particular portion size.
        """
        context = super().get_serializer_context()
        context["portion"] = self.request.GET.get('portion') or 1
        return context
