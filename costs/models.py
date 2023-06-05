from django.db import models
from django.utils import timezone



class HousingType(models.Model):
    HOUSING_CHOICES = [
        ('Studio Apartment', 'Studio Apartment'),
        ('1.5-Bedroom Apartment', '1.5-Bedroom Apartment'),
        ('2.5-Bedroom Apartment', '2.5-Bedroom Apartment'),
        ('3.5-Bedroom Apartment', '3.5-Bedroom Apartment'),
        ('4.5-Bedroom Apartment', '4.5-Bedroom Apartment'),
    ]

    type = models.CharField(max_length=50, choices=HOUSING_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.type

class HealthInsurance(models.Model):
    COVERAGE_CHOICES = [
        ('basic', 'Basic Coverage'),
        ('standard', 'Standard Coverage'),
        ('comprehensive', 'Comprehensive Coverage'),
        ('premium', 'Premium Coverage'),
        ('maximum', 'Maximum Coverage'),
    ]
    coverage = models.CharField(max_length=50, choices=COVERAGE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.coverage

class ElectricVehicle(models.Model):
    ELECTRICITY_CONSUMPTION_CHOICES = [
        ('low', 'Low (10-15 kWh/100km)'),
        ('medium', 'Medium (16-20 kWh/100km)'),
        ('high', 'High (21-25 kWh/100km)'),
        ('very_high', 'Very High (26+ kWh/100km)')
    ]

    DISTANCE_DRIVEN_CHOICES = [
        ('low', 'Low (0-20 km)'),
        ('medium', 'Medium (21-50 km)'),
        ('high', 'High (51-100 km)'),
        ('very_high', 'Very High (100+ km)')
    ]   

    electricity_consumption = models.CharField(max_length=50, choices=ELECTRICITY_CONSUMPTION_CHOICES)
    distance_driven = models.CharField(max_length=50, choices=DISTANCE_DRIVEN_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.electricity_consumption + " " + self.distance_driven    

class CombustionVehicle(models.Model):
    FUEL_TYPE_CHOICES = [
        ('diesel', 'Diesel'), 
        ('petrol', 'Petrol')
    ]

    FUEL_CONSUMPTION_CHOICES = [
        ('low', 'Low (1-5 L/100km)'),
        ('medium', 'Medium (6-10 L/100km)'),
        ('high', 'High (11-15 L/100km)'),
        ('very_high', 'Very High (16+ L/100km)')
    ]

    DISTANCE_DRIVEN_CHOICES = [
        ('low', 'Low (0-20 km)'),
        ('medium', 'Medium (21-50 km)'),
        ('high', 'High (51-100 km)'),
        ('very_high', 'Very High (100+ km)')
    ]

    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, default='diesel')
    fuel_consumption = models.CharField(max_length=50, choices=FUEL_CONSUMPTION_CHOICES)
    distance_driven = models.CharField(max_length=50, choices=DISTANCE_DRIVEN_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.fuel_type + " " + self.fuel_consumption + " " + self.distance_driven    

class PublicTransport(models.Model):
    USAGE_CHOICES = [
        ('rarely', 'Rarely'),
        ('occasionally', 'Occasionally'),
        ('weekly', 'Weekly'),
        ('daily', 'Daily')
    ]

    usage = models.CharField(max_length=50, choices=USAGE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.usage


class PhonePlan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('unlimited', 'Unlimited'),
    ]
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.plan


class InternetPlan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('high_speed', 'High-Speed'),
    ]
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.plan

class FoodBudget(models.Model):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.budget


class ClothingBudget(models.Model):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
        ('extreme', 'Extreme'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.budget

class Childcare(models.Model):
    CHILDCARE_CHOICES = [
        ('none', 'None'),
        ('home_based', 'Home-based Childcare'),
        ('daycare_center', 'Daycare Center'),
        ('nanny', 'Nanny'),
        ('au_pair', 'Au Pair'),
    ]
    childcare_type = models.CharField(max_length=50, choices=CHILDCARE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.childcare_type
    
class Education(models.Model):
    EDUCATION_CHOICES = [
        ('none', 'None'),
        ('public_school', 'Public School'),
        ('private_school', 'Private School'),
        ('international_school', 'International School'),
        ('university', 'University'),
    ]
    education_type = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.education_type

class EntertainmentAndLeisure(models.Model):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.budget

