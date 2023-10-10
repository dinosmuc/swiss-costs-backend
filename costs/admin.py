from django.contrib import admin
from .models import (Canton, Salary, Job, HousingType, HealthInsurance, PublicTransport, PhonePlan, InternetPlan, FoodBudget, 
                     ClothingBudget, Childcare, Education, EntertainmentAndLeisure, 
                     Age, MaritalStatus, ChurchMember, FuelPrice, ElectricityPrice)

admin.site.register(Canton)
admin.site.register(Salary)
admin.site.register(Job)
admin.site.register(Age)
admin.site.register(MaritalStatus)
admin.site.register(ChurchMember)
admin.site.register(HousingType)
admin.site.register(HealthInsurance)
admin.site.register(PublicTransport)
admin.site.register(PhonePlan)
admin.site.register(InternetPlan)
admin.site.register(FoodBudget)
admin.site.register(ClothingBudget)
admin.site.register(Childcare)
admin.site.register(Education)
admin.site.register(EntertainmentAndLeisure)
admin.site.register(FuelPrice)
admin.site.register(ElectricityPrice)
