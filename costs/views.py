from rest_framework import viewsets
from .models import (HousingType, HealthInsurance, ElectricVehicle, CombustionVehicle, PublicTransport, 
                     PhonePlan, InternetPlan, FoodBudget, ClothingBudget, Childcare, Education, 
                     EntertainmentAndLeisure)
from .serializers import (HousingTypeSerializer, HealthInsuranceSerializer, ElectricVehicleSerializer, 
                          CombustionVehicleSerializer, PublicTransportSerializer, PhonePlanSerializer, 
                          InternetPlanSerializer, FoodBudgetSerializer, ClothingBudgetSerializer, 
                          ChildcareSerializer, EducationSerializer, EntertainmentAndLeisureSerializer)

class HousingTypeViewSet(viewsets.ModelViewSet):
    queryset = HousingType.objects.all()
    serializer_class = HousingTypeSerializer

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer

class ElectricVehicleViewSet(viewsets.ModelViewSet):
    queryset = ElectricVehicle.objects.all()
    serializer_class = ElectricVehicleSerializer

class CombustionVehicleViewSet(viewsets.ModelViewSet):
    queryset = CombustionVehicle.objects.all()
    serializer_class = CombustionVehicleSerializer

class PublicTransportViewSet(viewsets.ModelViewSet):
    queryset = PublicTransport.objects.all()
    serializer_class = PublicTransportSerializer

class PhonePlanViewSet(viewsets.ModelViewSet):
    queryset = PhonePlan.objects.all()
    serializer_class = PhonePlanSerializer

class InternetPlanViewSet(viewsets.ModelViewSet):
    queryset = InternetPlan.objects.all()
    serializer_class = InternetPlanSerializer

class FoodBudgetViewSet(viewsets.ModelViewSet):
    queryset = FoodBudget.objects.all()
    serializer_class = FoodBudgetSerializer

class ClothingBudgetViewSet(viewsets.ModelViewSet):
    queryset = ClothingBudget.objects.all()
    serializer_class = ClothingBudgetSerializer

class ChildcareViewSet(viewsets.ModelViewSet):
    queryset = Childcare.objects.all()
    serializer_class = ChildcareSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EntertainmentAndLeisureViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentAndLeisure.objects.all()
    serializer_class = EntertainmentAndLeisureSerializer
