from rest_framework import serializers
from .models import (HousingType, HealthInsurance, ElectricVehicle, CombustionVehicle, PublicTransport, 
                     PhonePlan, InternetPlan, FoodBudget, ClothingBudget, Childcare, Education, 
                     EntertainmentAndLeisure)

class HousingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingType
        fields = '__all__'

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
        fields = '__all__'

class ElectricVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricVehicle
        fields = '__all__'

class CombustionVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombustionVehicle
        fields = '__all__'

class PublicTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicTransport
        fields = '__all__'

class PhonePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonePlan
        fields = '__all__'

class InternetPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetPlan
        fields = '__all__'

class FoodBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodBudget
        fields = '__all__'

class ClothingBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingBudget
        fields = '__all__'

class ChildcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childcare
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EntertainmentAndLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentAndLeisure
        fields = '__all__'
