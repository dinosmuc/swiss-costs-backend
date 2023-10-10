from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'entertainment_and_leisure', views.EntertainmentAndLeisureViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'childcare', views.ChildcareViewSet)
router.register(r'clothing_budget', views.ClothingBudgetViewSet)
router.register(r'food_budget', views.FoodBudgetViewSet)
router.register(r'internet_plan', views.InternetPlanViewSet)
router.register(r'phone_plan', views.PhonePlanViewSet)
router.register(r'public_transport', views.PublicTransportViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Existing API routes
    path('api/calculate_insurance_cost/', views.calculate_insurance_cost),
    path('api/calculate_housing_cost/', views.calculate_housing_cost),
    path('api/calculate_combustion_vehicle_cost/', views.calculate_combustion_vehicle_cost),
    path('api/calculate_electric_vehicle_cost/', views.calculate_electric_vehicle_cost),
    path('api/calculate_neto_salary/', views.calculate_neto_salary),
    path('api/get_salary_by_job_title/', views.get_salary_by_job_title),
]
