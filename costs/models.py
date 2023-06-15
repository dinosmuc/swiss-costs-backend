from django.db import models
from django.utils import timezone


def current_year():
    return timezone.now().year

class ValueModel(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        abstract = True

class Canton(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class User(models.Model):
    # Personal Information
    MARTIAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('MSI', 'Married with a single income'),
        ('MDI', 'Married with a double income'),
        ('SP', 'Single parent'),
    ]
    CHURCH_MEMBERSHIP_CHOICES = [
    ('church_member', 'A church member'),
    ('not_church_member', 'Not a church member')
]
    AGE_CHOICES = [(i, str(i)) for i in range(18, 101)]  # Age from 18 to 100

    year = models.PositiveIntegerField(default=current_year)
    marital_status = models.CharField(max_length=3, choices=MARTIAL_STATUS_CHOICES, default='S')
    church_member = models.CharField(max_length=20, choices=CHURCH_MEMBERSHIP_CHOICES, default='not_church_member')
    age = models.IntegerField(choices=AGE_CHOICES)

    # Family Information
    CHILDREN_CHOICES = [(i, str(i)) for i in range(10)]  # 0 to 9 children

    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    num_children = models.IntegerField(choices=CHILDREN_CHOICES)

class Salary(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Job(models.Model):
    
    job_title = models.CharField(max_length=50)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.job_title



class HousingType(ValueModel):
    HOUSING_CHOICES = [
        ('studio', 'Studio Apartment'),
        ('1.5_bedroom', '1.5-Bedroom Apartment'),
        ('2.5_bedroom', '2.5-Bedroom Apartment'),
        ('3.5_bedroom', '3.5-Bedroom Apartment'),
        ('4.5_bedroom', '4.5-Bedroom Apartment'),
    ]

    type = models.CharField(max_length=50, choices=HOUSING_CHOICES)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE, related_name='housing_types')

    def __str__(self):
        return self.get_type_display() + " in " + self.canton.name

class HealthInsurance(ValueModel):
    COVERAGE_CHOICES = [
        ('basic', 'Basic Coverage'),
        ('standard', 'Standard Coverage'),
        ('comprehensive', 'Comprehensive Coverage'),
        ('premium', 'Premium Coverage'),
        ('maximum', 'Maximum Coverage'),
    ]
    coverage = models.CharField(max_length=50, choices=COVERAGE_CHOICES)
    def __str__(self):
        return self.coverage

class ElectricVehicle(ValueModel):
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
    def __str__(self):
        return self.electricity_consumption + " " + self.distance_driven    

class CombustionVehicle(ValueModel):
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
    def __str__(self):
        return self.fuel_type + " " + self.fuel_consumption + " " + self.distance_driven    

class PublicTransport(ValueModel):
    USAGE_CHOICES = [
        ('rarely', 'Rarely'),
        ('occasionally', 'Occasionally'),
        ('weekly', 'Weekly'),
        ('daily', 'Daily')
    ]

    usage = models.CharField(max_length=50, choices=USAGE_CHOICES)
    def __str__(self):
        return self.usage


class PhonePlan(ValueModel):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('unlimited', 'Unlimited'),
    ]
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    def __str__(self):
        return self.plan


class InternetPlan(ValueModel):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('high_speed', 'High-Speed'),
    ]
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    def __str__(self):
        return self.plan

class FoodBudget(ValueModel):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    def __str__(self):
        return self.budget


class ClothingBudget(ValueModel):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
        ('extreme', 'Extreme'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    def __str__(self):
        return self.budget

class Childcare(ValueModel):
    CHILDCARE_CHOICES = [
        ('none', 'None'),
        ('home_based', 'Home-based Childcare'),
        ('daycare_center', 'Daycare Center'),
        ('nanny', 'Nanny'),
        ('au_pair', 'Au Pair'),
    ]
    childcare_type = models.CharField(max_length=50, choices=CHILDCARE_CHOICES)
    def __str__(self):
        return self.childcare_type
    
class Education(ValueModel):
    EDUCATION_CHOICES = [
        ('none', 'None'),
        ('public_school', 'Public School'),
        ('private_school', 'Private School'),
        ('international_school', 'International School'),
        ('university', 'University'),
    ]
    education_type = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    def __str__(self):
        return self.education_type

class EntertainmentAndLeisure(ValueModel):
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    def __str__(self):
        return self.budget

