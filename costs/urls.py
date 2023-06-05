from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (HousingTypeViewSet, HealthInsuranceViewSet, ElectricVehicleViewSet, 
                    CombustionVehicleViewSet, PublicTransportViewSet, PhonePlanViewSet, 
                    InternetPlanViewSet, FoodBudgetViewSet, ClothingBudgetViewSet, 
                    ChildcareViewSet, EducationViewSet, EntertainmentAndLeisureViewSet)

router = DefaultRouter()
router.register(r'housing-types', HousingTypeViewSet)
router.register(r'health-insurances', HealthInsuranceViewSet)
router.register(r'electric-vehicles', ElectricVehicleViewSet)
router.register(r'combustion-vehicles', CombustionVehicleViewSet)
router.register(r'public-transports', PublicTransportViewSet)
router.register(r'phone-plans', PhonePlanViewSet)
router.register(r'internet-plans', InternetPlanViewSet)
router.register(r'food-budgets', FoodBudgetViewSet)
router.register(r'clothing-budgets', ClothingBudgetViewSet)
router.register(r'childcares', ChildcareViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'entertainment-and-leisures', EntertainmentAndLeisureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
