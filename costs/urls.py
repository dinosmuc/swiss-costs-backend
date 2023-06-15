from django.urls import path
from .views import calculate_expenses

urlpatterns = [
    path('calculate_expenses/', calculate_expenses, name='calculate_expenses'),  # Added URL pattern for expense_calculation
]