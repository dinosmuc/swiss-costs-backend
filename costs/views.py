from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json

from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import viewsets
from .models import EntertainmentAndLeisure, Education, Childcare,ClothingBudget, FoodBudget, InternetPlan,PhonePlan,PublicTransport,FuelPrice, ElectricityPrice
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

        print(data)
        
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
    'Human Resources Manager': 90000,
    'Pharmaceutical Researcher': 120000,
    'Doctor (General Practitioner)': 140000,
    'Nurse': 75000,
    'Dentist': 130000,
    'Architect': 95000,
    'Lawyer': 130000,
    'Banker': 110000,
    'IT Manager': 115000,
    'Consultant': 110000,
    'Tax Advisor': 105000,
    'Pharmacist': 100000,
    'Research Scientist': 100000,
    'Teacher': 75000,
    'Accountant': 95000,
    'Chef': 70000,
    'Hotel Manager': 90000,
    'Real Estate Agent': 80000,
    'Policeman': 80000,
    'Journalist': 80000,
    'Biotechnologist': 110000,
    'Physiotherapist': 80000,
    'Veterinarian': 95000,
    'Social Worker': 70000,
    'Psychologist': 90000,
    'Insurance Agent': 85000,
    'Electrician': 75000,
    'Plumber': 73000,
    'Construction Worker': 65000,
    'Agricultural Engineer': 85000,
    'Waiter/Waitress': 45000,
    'Barista': 45000,
    'Shop Assistant': 48000,
    'Bus Driver': 60000,
    'Pilot': 140000,
    'Flight Attendant': 65000,
    'Postman': 65000,
    'Librarian': 70000,
    'Pharmacy Assistant': 60000,
    'Cleaner': 42000,
    'Auditor': 95000,
    'Translator': 80000,
    'Systems Administrator': 90000,
    'Database Administrator': 95000,
    'Retail Manager': 80000,
    'Surgeon': 230000,
    'Pharmacy Technician': 65000,
    'Medical Assistant': 60000,
    'Optometrist': 110000,
    'Dietitian': 75000,
    'Radiologic Technologist': 85000,
    'Dental Hygienist': 70000,
    'Medical Laboratory Technician': 70000,
    'Logistics Manager': 95000,
    'Supply Chain Manager': 98000,
    'Web Developer': 95000,
    'UX/UI Designer': 90000,
    'Interior Designer': 85000,
    'Environmental Scientist': 90000,
    'Audiologist': 90000,
    'Occupational Therapist': 80000,
    'Speech-Language Pathologist': 80000,
    'Zoologist': 80000,
    'Bakery Chef': 65000,
    'Butcher': 60000,
    'Fishmonger': 58000,
    'Public Relations Specialist': 90000,
    'Recruiter': 90000,
    'Tour Guide': 50000,
    'Travel Agent': 60000,
    'Taxi Driver': 50000,
    'Train Conductor': 70000,
    'Economist': 100000,
    'Geologist': 95000,
    'Petroleum Engineer': 120000,
    'Astronomer': 90000,
    'Astrophysicist': 95000,
    'Meteorologist': 90000,
    'Statistician': 98000,
    'Mathematician': 95000,
    'Carpenter': 70000,
    'Bricklayer': 65000,
    'Landscaper': 60000,
    'Florist': 55000,
    'Gardener': 55000,
    'Real Estate Developer': 110000,
    'Hair Stylist': 50000,
    'Makeup Artist': 60000,
    'Fashion Designer': 85000,
    'Seamstress/Tailor': 55000,
    'Dancer': 50000,
    'Actor': 55000,
    'Cinematographer': 80000
}
   

@api_view(['GET'])
def calculate_housing_cost(request):
    canton = request.GET.get('canton', '')
    housingType = request.GET.get('housing_Type', '')
    

    cost = 0

    if canton == 'Zug':

        if housingType == 'room':
            cost = 800
        elif housingType == 'studio':
            cost = 1000
        elif housingType == '1.5_bedroom':
            cost = 1300
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1800
        elif housingType == '4.5_bedroom':
            cost = 2200

    elif canton == 'Zürich':

        if housingType == 'room':
            cost =  900
        elif housingType == 'studio':
            cost = 1200
        elif housingType == '1.5_bedroom':
            cost = 1500
        elif housingType == '2.5_bedroom':
            cost = 2000
        elif housingType == '3.5_bedroom':
            cost = 2300
        elif housingType == '4.5_bedroom':
            cost = 2700

    elif canton == 'Bern':
    
        if housingType == 'room':
            cost = 700
        elif housingType == 'studio':
            cost = 1100
        elif housingType == '1.5_bedroom':
            cost = 1400
        elif housingType == '2.5_bedroom':
            cost = 1700
        elif housingType == '3.5_bedroom':
            cost = 2000
        elif housingType == '4.5_bedroom':
            cost = 2400

    elif canton == 'Geneva':
        
        if housingType == 'room':
            cost = 1000
        elif housingType == 'studio':
            cost = 1400
        elif housingType == '1.5_bedroom':
            cost = 1800
        elif housingType == '2.5_bedroom':
            cost = 2200
        elif housingType == '3.5_bedroom':
            cost = 2600
        elif housingType == '4.5_bedroom':
            cost = 3100

    elif canton == 'Valais':
        
        if housingType == 'room':
            cost = 600
        elif housingType == 'studio':
            cost = 900
        elif housingType == '1.5_bedroom':
            cost = 1200
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1800
        elif housingType == '4.5_bedroom':
            cost = 2100

    elif canton == 'Vaud':
        
        if housingType == 'room':
            cost = 800
        elif housingType == 'studio':
            cost = 1200
        elif housingType == '1.5_bedroom':
            cost = 1500
        elif housingType == '2.5_bedroom':
            cost = 1900
        elif housingType == '3.5_bedroom':
            cost = 2200
        elif housingType == '4.5_bedroom':
            cost = 2600


    elif canton == 'Basel-Stadt':

        if housingType == 'room':
            cost = 750
        elif housingType == 'studio':
            cost = 1150
        elif housingType == '1.5_bedroom':
            cost = 1450
        elif housingType == '2.5_bedroom':
            cost = 1800
        elif housingType == '3.5_bedroom':
            cost = 2150
        elif housingType == '4.5_bedroom':
            cost = 2500

    elif canton == 'Graubünden':

        if housingType == 'room':
            cost = 650
        elif housingType == 'studio':
            cost = 950
        elif housingType == '1.5_bedroom':
            cost = 1250
        elif housingType == '2.5_bedroom':
            cost = 1550
        elif housingType == '3.5_bedroom':
            cost = 1850
        elif housingType == '4.5_bedroom':
            cost = 2200

    elif canton == 'Lucerne':

        if housingType == 'room':
            cost = 700
        elif housingType == 'studio':
            cost = 1100
        elif housingType == '1.5_bedroom':
            cost = 1400
        elif housingType == '2.5_bedroom':
            cost = 1750
        elif housingType == '3.5_bedroom':
            cost = 2100
        elif housingType == '4.5_bedroom':
            cost = 2450

    elif canton == 'St. Gallen':

        if housingType == 'room':
            cost = 650
        elif housingType == 'studio':
            cost = 1000
        elif housingType == '1.5_bedroom':
            cost = 1300
        elif housingType == '2.5_bedroom':
            cost = 1600
        elif housingType == '3.5_bedroom':
            cost = 1950
        elif housingType == '4.5_bedroom':
            cost = 2300

    elif canton == 'Aargau':

        if housingType == 'room':
            cost = 600
        elif housingType == 'studio':
            cost = 950
        elif housingType == '1.5_bedroom':
            cost = 1250
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1850
        elif housingType == '4.5_bedroom':
            cost = 2150

    elif canton == 'Fribourg':

        if housingType == 'room':
            cost = 650
        elif housingType == 'studio':
            cost = 1000
        elif housingType == '1.5_bedroom':
            cost = 1300
        elif housingType == '2.5_bedroom':
            cost = 1600
        elif housingType == '3.5_bedroom':
            cost = 1900
        elif housingType == '4.5_bedroom':
            cost = 2200

    elif canton == 'Ticino':

        if housingType == 'room':
            cost = 700
        elif housingType == 'studio':
            cost = 1050
        elif housingType == '1.5_bedroom':
            cost = 1350
        elif housingType == '2.5_bedroom':
            cost = 1650
        elif housingType == '3.5_bedroom':
            cost = 2000
        elif housingType == '4.5_bedroom':
            cost = 2350

    elif canton == 'Neuchâtel':

        if housingType == 'room':
            cost = 650
        elif housingType == 'studio':
            cost = 1000
        elif housingType == '1.5_bedroom':
            cost = 1300
        elif housingType == '2.5_bedroom':
            cost = 1600
        elif housingType == '3.5_bedroom':
            cost = 1950
        elif housingType == '4.5_bedroom':
            cost = 2250

    elif canton == 'Thurgau':

        if housingType == 'room':
            cost = 580
        elif housingType == 'studio':
            cost = 930
        elif housingType == '1.5_bedroom':
            cost = 1200
        elif housingType == '2.5_bedroom':
            cost = 1475
        elif housingType == '3.5_bedroom':
            cost = 1800
        elif housingType == '4.5_bedroom':
            cost = 2100

    elif canton == 'Schaffhausen':

        if housingType == 'room':
            cost = 600
        elif housingType == 'studio':
            cost = 950
        elif housingType == '1.5_bedroom':
            cost = 1275
        elif housingType == '2.5_bedroom':
            cost = 1575
        elif housingType == '3.5_bedroom':
            cost = 1900
        elif housingType == '4.5_bedroom':
            cost = 2225

    elif canton == 'Jura':

        if housingType == 'room':
            cost = 570
        elif housingType == 'studio':
            cost = 900
        elif housingType == '1.5_bedroom':
            cost = 1175
        elif housingType == '2.5_bedroom':
            cost = 1450
        elif housingType == '3.5_bedroom':
            cost = 1750
        elif housingType == '4.5_bedroom':
            cost = 2050

    elif canton == 'Appenzell Innerrhoden':

        if housingType == 'room':
            cost = 600
        elif housingType == 'studio':
            cost = 925
        elif housingType == '1.5_bedroom':
            cost = 1225
        elif housingType == '2.5_bedroom':
            cost = 1525
        elif housingType == '3.5_bedroom':
            cost = 1825
        elif housingType == '4.5_bedroom':
            cost = 2150

    elif canton == 'Appenzell Ausserrhoden':

        if housingType == 'room':
            cost = 590
        elif housingType == 'studio':
            cost = 915
        elif housingType == '1.5_bedroom':
            cost = 1195
        elif housingType == '2.5_bedroom':
            cost = 1475
        elif housingType == '3.5_bedroom':
            cost = 1775
        elif housingType == '4.5_bedroom':
            cost = 2090

    elif canton == 'Obwalden':

        if housingType == 'room':
            cost = 610
        elif housingType == 'studio':
            cost = 940
        elif housingType == '1.5_bedroom':
            cost = 1210
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1820
        elif housingType == '4.5_bedroom':
            cost = 2135

    elif canton == 'Nidwalden':

        if housingType == 'room':
            cost = 625
        elif housingType == 'studio':
            cost = 955
        elif housingType == '1.5_bedroom':
            cost = 1235
        elif housingType == '2.5_bedroom':
            cost = 1525
        elif housingType == '3.5_bedroom':
            cost = 1850
        elif housingType == '4.5_bedroom':
            cost = 2165

    elif canton == 'Uri':

        if housingType == 'room':
            cost = 595
        elif housingType == 'studio':
            cost = 925
        elif housingType == '1.5_bedroom':
            cost = 1205
        elif housingType == '2.5_bedroom':
            cost = 1490
        elif housingType == '3.5_bedroom':
            cost = 1790
        elif housingType == '4.5_bedroom':
            cost = 2100

    elif canton == 'Schwyz':
        
        if housingType == 'room':
            cost = 610
        elif housingType == 'studio':
            cost = 940
        elif housingType == '1.5_bedroom':
            cost = 1220
        elif housingType == '2.5_bedroom':
            cost = 1500
        elif housingType == '3.5_bedroom':
            cost = 1820
        elif housingType == '4.5_bedroom':
            cost = 2135
            
    elif canton == 'Glarus':

        if housingType == 'room':
            cost = 600
        elif housingType == 'studio':
            cost = 930
        elif housingType == '1.5_bedroom':
            cost = 1200
        elif housingType == '2.5_bedroom':
            cost = 1480
        elif housingType == '3.5_bedroom':
            cost = 1780
        elif housingType == '4.5_bedroom':
            cost = 2080
            
    elif canton == 'Solothurn':

        if housingType == 'room':
            cost = 615
        elif housingType == 'studio':
            cost = 945
        elif housingType == '1.5_bedroom':
            cost = 1215
        elif housingType == '2.5_bedroom':
            cost = 1515
        elif housingType == '3.5_bedroom':
            cost = 1815
        elif housingType == '4.5_bedroom':
            cost = 2130
            
    elif canton == 'Basel-Landschaft':

        if housingType == 'room':
            cost = 620
        elif housingType == 'studio':
            cost = 950
        elif housingType == '1.5_bedroom':
            cost = 1230
        elif housingType == '2.5_bedroom':
            cost = 1530
        elif housingType == '3.5_bedroom':
            cost = 1830
        elif housingType == '4.5_bedroom':
            cost = 2145

    return Response({'cost': cost}, status=status.HTTP_200_OK)


@api_view(['GET'])
def calculate_neto_salary(request):
    bruto_salary = int(request.GET.get('bruto_salary', 0))

    print(f"Debug: Received bruto_salary: {bruto_salary}")

    neto_salary = int(bruto_salary * 0.85)

    

    return Response({'neto_salary': neto_salary}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_salary_by_job_title(request):

    print("Debug: Entered get_salary_by_job_title function")

    job_title = request.GET.get('job_title', '')

    print(f"Debug: Received job title: {job_title}")

    gross_salary = JOB_TITLE_TO_GROSS_SALARY.get(job_title, 0)

    print(f"Debug: Calculated gross salary: {gross_salary}")

    neto_salary = gross_salary * 0.85 / 13
    gross_salary = int(gross_salary / 13)

    print(f"Debug: Calculated neto_salary: {neto_salary}")
    return Response({'neto_salary': neto_salary, "gross_salary": gross_salary}, status=status.HTTP_200_OK)
