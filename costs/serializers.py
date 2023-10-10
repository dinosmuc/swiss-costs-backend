from rest_framework import serializers
from .models import EntertainmentAndLeisure,Education, Childcare, ClothingBudget, FoodBudget, InternetPlan, PhonePlan, PublicTransport

class EntertainmentAndLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentAndLeisure
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ChildcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childcare
        fields = '__all__'

class ClothingBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingBudget
        fields = '__all__'

class FoodBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodBudget
        fields = '__all__'

class InternetPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetPlan
        fields = '__all__'

class PhonePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonePlan
        fields = '__all__'

class PublicTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicTransport
        fields = '__all__'

