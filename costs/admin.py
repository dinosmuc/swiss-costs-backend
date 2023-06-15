from django.contrib import admin
from .models import (User, Canton, Salary, Job, HousingType, HealthInsurance, ElectricVehicle, CombustionVehicle, PublicTransport, 
                     PhonePlan, InternetPlan, FoodBudget, ClothingBudget, Childcare, Education, 
                     EntertainmentAndLeisure)

admin.site.register(Canton)
admin.site.register(HousingType)
admin.site.register(HealthInsurance)
admin.site.register(ElectricVehicle)
admin.site.register(CombustionVehicle)
admin.site.register(PublicTransport)
admin.site.register(PhonePlan)
admin.site.register(InternetPlan)
admin.site.register(FoodBudget)
admin.site.register(ClothingBudget)
admin.site.register(Childcare)
admin.site.register(Education)
admin.site.register(EntertainmentAndLeisure)
admin.site.register(Salary)
admin.site.register(Job)
admin.site.register(User)   