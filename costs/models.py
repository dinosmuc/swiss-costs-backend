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



# Age Model
class Age(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(18, 101)]
    age = models.IntegerField(choices=AGE_CHOICES, )

# Marital Status Model
class MaritalStatus(models.Model):
    MARTIAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('MSI', 'Married with a single income'),
        ('MDI', 'Married with a double income'),
        ('SP', 'Single parent'),
    ]
    status = models.CharField(max_length=3, choices=MARTIAL_STATUS_CHOICES)

# Church Member Model
class ChurchMember(models.Model):
    CHURCH_MEMBERSHIP_CHOICES = [
        ('church_member', 'A church member'),
        ('not_church_member', 'Not a church member')
    ]
    membership = models.CharField(max_length=20, choices=CHURCH_MEMBERSHIP_CHOICES)

# Salary Model
class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

# Job Model
class Job(models.Model):
    title = models.CharField(max_length=50)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class HousingType(models.Model):
    HOUSING_CHOICES = [
        ('studio', 'Studio Apartment'),
        ('1.5_bedroom', '1.5-Bedroom Apartment'),
        ('2.5_bedroom', '2.5-Bedroom Apartment'),
        ('3.5_bedroom', '3.5-Bedroom Apartment'),
        ('4.5_bedroom', '4.5-Bedroom Apartment'),
    ]

    type = models.CharField(max_length=50, choices=HOUSING_CHOICES)
    

    def __str__(self):
        return f"{self.get_type_display()} in {self.canton.name}"




class HealthInsurance(models.Model):
    COVERAGE_CHOICES = [
        ('basic', 'Basic Coverage'),
        ('standard', 'Standard Coverage'),
        ('comprehensive', 'Comprehensive Coverage'),
        ('premium', 'Premium Coverage'),
        ('maximum', 'Maximum Coverage'),
    ]
    
    coverage = models.CharField(max_length=50, choices=COVERAGE_CHOICES)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, null=True)  # Linking Age to HealthInsurance
    cost = models.FloatField(default=0)  # Add a cost field
    
    def calculate_cost(self):
        if self.age.age >= 18 and self.age.age <= 30:
            if self.coverage == 'basic':
                return 200
            elif self.coverage == 'standard':
                return 300
            elif self.coverage == 'comprehensive':
                return 400
            elif self.coverage == 'premium':
                return 500
            elif self.coverage == 'maximum':
                return 600
        elif self.age.age > 30 and self.age.age <= 50:
            if self.coverage == 'basic':
                return 250
            elif self.coverage == 'standard':
                return 350
            elif self.coverage == 'comprehensive':
                return 450
            elif self.coverage == 'premium':
                return 550
            elif self.coverage == 'maximum':
                return 650
        else:  # for age > 50
            if self.coverage == 'basic':
                return 300
            elif self.coverage == 'standard':
                return 400
            elif self.coverage == 'comprehensive':
                return 500
            elif self.coverage == 'premium':
                return 600
            elif self.coverage == 'maximum':
                return 700
    
    def save(self, *args, **kwargs):
        self.cost = self.calculate_cost()
        super().save(*args, **kwargs)





class FuelPrice(models.Model):
    diesel_price = models.FloatField("Price of Diesel per liter", default=0)
    petrol_price = models.FloatField("Price of Petrol per liter", default=0)
    
    def __str__(self):
        return f"Diesel: {self.diesel_price} CHF, Petrol: {self.petrol_price} CHF"


class ElectricityPrice(models.Model):
    price_per_kWh = models.FloatField("Price per kWh", default=0)

    def __str__(self):
        return f"Electricity: {self.price_per_kWh} CHF/kWh"



class PublicTransport(ValueModel):
    USAGE_CHOICES = [
        ('never', 'Never'),
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
        ('none', 'None'),
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
        ('none', 'None'),
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('high_speed', 'High-Speed'),
    ]
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    def __str__(self):
        return self.plan

class FoodBudget(ValueModel):
    BUDGET_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('moderate_low', 'Moderate Low'),
        ('medium', 'Medium'),
        ('moderate_high', 'Moderate High'),
        ('high', 'High'),
        ('very_high', 'Very High'),
        ('extreme', 'Extreme'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    
    def __str__(self):
        return self.budget



class ClothingBudget(ValueModel):
    BUDGET_CHOICES = [
        ('none', 'None'),
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
        ('none', 'None'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    def __str__(self):
        return self.budget

