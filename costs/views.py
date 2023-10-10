from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json

from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import viewsets
from .models import EntertainmentAndLeisure, Education, Childcare, ClothingBudget, FoodBudget, InternetPlan, PhonePlan, PublicTransport,FuelPrice, ElectricityPrice
from .serializers import EntertainmentAndLeisureSerializer, EducationSerializer, ChildcareSerializer, ClothingBudgetSerializer, FoodBudgetSerializer, InternetPlanSerializer, PhonePlanSerializer, PublicTransportSerializer


class EntertainmentAndLeisureViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentAndLeisure.objects.all().order_by('budget')
    serializer_class = EntertainmentAndLeisureSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('education_type')
    serializer_class = EducationSerializer


class ChildcareViewSet(viewsets.ModelViewSet):
    queryset = Childcare.objects.all().order_by('childcare_type')
    serializer_class = ChildcareSerializer

class ClothingBudgetViewSet(viewsets.ModelViewSet):
    queryset = ClothingBudget.objects.all().order_by('budget')
    serializer_class = ClothingBudgetSerializer

class FoodBudgetViewSet(viewsets.ModelViewSet):
    queryset = FoodBudget.objects.all().order_by('budget')
    serializer_class = FoodBudgetSerializer

class InternetPlanViewSet(viewsets.ModelViewSet):
    queryset = InternetPlan.objects.all().order_by('plan')
    serializer_class = InternetPlanSerializer

class PhonePlanViewSet(viewsets.ModelViewSet):
    queryset = PhonePlan.objects.all().order_by('plan')
    serializer_class = PhonePlanSerializer

class PublicTransportViewSet(viewsets.ModelViewSet):
    queryset = PublicTransport.objects.all().order_by('id')
    serializer_class = PublicTransportSerializer

@api_view(['GET'])
def calculate_insurance_cost(request):
    age = int(request.GET.get('age', 0))
    coverage = request.GET.get('coverage', '')

    # Initialize cost to 0
    cost = 0
    
    # Calculate cost based on age and coverage
    if age >= 18 and age <= 30:
        if coverage == 'basic_coverage':
            cost = 200
        elif coverage == 'standard_coverage':
            cost = 300
        elif coverage == 'comprehensive_coverage':
            cost = 400
        elif coverage == 'premium_coverage':
            cost = 500
        elif coverage == 'maximum_coverage':
            cost = 600
    elif age > 30 and age <= 50:
        if coverage == 'basic_coverage':
            cost = 250
        elif coverage == 'standard_coverage':
            cost = 350
        elif coverage == 'comprehensive_coverage':
            cost = 450
        elif coverage == 'premium_coverage':
            cost = 550
        elif coverage == 'maximum_coverage':
            cost = 650
    else:  # for age > 50
        if coverage == 'basic_coverage':
            cost = 300
        elif coverage == 'standard_coverage':
            cost = 400
        elif coverage == 'comprehensive_coverage':
            cost = 500
        elif coverage == 'premium_coverage':
            cost = 600
        elif coverage == 'maximum_coverage':
            cost = 700


    # Return the calculated cost
    return Response({'cost': cost}, status=status.HTTP_200_OK)


def get_latest_prices():
    # Fetch the single entry from the database
    fuel_price = FuelPrice.objects.first()
    electricity_price = ElectricityPrice.objects.first()
    return fuel_price, electricity_price


@csrf_exempt
def calculate_combustion_vehicle_cost(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        try:
            latest_fuel_prices = FuelPrice.objects.latest('id')
            fuel_type = data['fuelType']
            fuel_consumption = data['fuelConsumption']
            distance_driven = data['distanceDriven']
            
            actual_fuel_price = getattr(latest_fuel_prices, f"{fuel_type}_price")
            
            # Define the fuel consumption ranges (in L/100km) for each category
            fuel_consumption_values = {'low': 4, 'medium': 9, 'high': 14, 'very_high': 17}
            
            # Define the distance ranges (in km) for each category
            distance_values = {'low': 10, 'medium': 35, 'high': 70, 'very_high': 150}
            
            single_consumption = fuel_consumption_values[fuel_consumption]
            single_distance = distance_values[distance_driven]
            
            calculated_cost = (single_consumption / 100) * single_distance * actual_fuel_price * 30
            
            return JsonResponse({'calculated_cost': round(calculated_cost, 2)})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def calculate_electric_vehicle_cost(request):
    try:
        latest_electricity_price = ElectricityPrice.objects.latest('id')
    except ElectricityPrice.DoesNotExist:
        return JsonResponse({'error': 'No electricity prices found.'}, status=404)

    # Učitaj JSON payload iz dolaznog zahtjeva
    data = json.loads(request.body.decode('utf-8'))
    electricity_consumption = data.get('electricityConsumption', 'medium')  # Pretpostavljena vrijednost je 'medium'
    distance = data.get('distanceDriven', 'medium')  # Pretpostavljena vrijednost je 'medium'
    
    # Ovdje su predefinirane vrijednosti, možeš ih mijenjati po potrebi
    electricity_consumption_values = {
        'low': 13,
        'medium': 18,
        'high': 23,
        'very_high': 27,  
    }
    distance_values = {
        'low': 10,
        'medium': 35,
        'high': 70,
        'very_high': 150,
    }

    # Izračunaj troškove na temelju dolaznih podataka
    single_consumption = electricity_consumption_values[electricity_consumption]
    single_distance = distance_values[distance]
    actual_electricity_price = latest_electricity_price.price_per_kWh
    calculated_cost = (single_consumption / 100) * single_distance * actual_electricity_price * 30
    
    return JsonResponse({'calculated_cost': round(calculated_cost, 2)})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Your dictionary for job titles to gross salaries
JOB_TITLE_TO_GROSS_SALARY = {
    'Software Engineer': 100000,
    'Data Scientist': 110000,
    'Marketing Manager': 90000,
    'Sales Manager': 95000,
    'Mechanical Engineer': 92000,
    'Civil Engineer': 88000,
    'Financial Analyst': 98000,
    'Project Manager': 105000,
    'Graphic Designer': 85000,
    'Human Resources Manager': 90000
}
   

@api_view(['GET'])
def calculate_housing_cost(request):
    canton = request.GET.get('canton', '')
    housingType = request.GET.get('housing_Type', '')
    

    cost = 0

    if canton == 'Zug':

        if housingType == 'studio':
            cost = 800
        elif housingType == '1.5_bedroom':
            cost = 1300
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1800
        elif housingType == '4.5_bedroom':
            cost = 2200

    elif canton == 'Zürich':

        if housingType == 'studio':
            cost = 1000
        elif housingType == '1.5_bedroom':
            cost = 1500
        elif housingType == '2.5_bedroom':
            cost = 2000
        elif housingType == '3.5_bedroom':
            cost = 2300
        elif housingType == '4.5_bedroom':
            cost = 2700

        return Response({'cost': cost}, status=status.HTTP_200_OK)


@api_view(['GET'])
def calculate_neto_salary(request):
    bruto_salary = int(request.GET.get('bruto_salary', 0))
    

    neto_salary = bruto_salary * 0.85

    return Response({'neto_salary': neto_salary}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_salary_by_job_title(request):

    print("Debug: Entered get_salary_by_job_title function")

    job_title = request.GET.get('job_title', '')

    print(f"Debug: Received job title: {job_title}")

    gross_salary = JOB_TITLE_TO_GROSS_SALARY.get(job_title, 0)

    print(f"Debug: Calculated gross salary: {gross_salary}")

    neto_salary = gross_salary * 0.85 / 13

    print(f"Debug: Calculated neto_salary: {neto_salary}")
    return Response({'neto_salary': neto_salary}, status=status.HTTP_200_OK)
