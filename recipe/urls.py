from django.urls import path

from .views import *

urlpatterns = [
    path('recipe/', ListRecipe.as_view(), name='token_obtain_pair'),
    path('recipe/<int:pk>', RetrieveRecipe.as_view(), name='token_refresh'),
]
