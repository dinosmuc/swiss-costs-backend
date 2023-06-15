from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import json



from .models import (Canton, User, Job, Salary, HousingType, HealthInsurance, 
                     ElectricVehicle, CombustionVehicle, PublicTransport, 
                     PhonePlan, InternetPlan, FoodBudget, ClothingBudget, 
                     Childcare, Education, EntertainmentAndLeisure)


@csrf_exempt
def calculate_expenses(request):
    print("Calculate expenses view was hit!")
    if request.method == 'POST':
        data = json.loads(request.body)

        # Retrieve the salary, housing type, childcare type, canton, and health insurance data from the JSON data
        salary_data = Decimal(data.get('salary')) 
        housing_type_data = data.get('housingType', {}).get('type')
        canton_data = data.get('user', {}).get('canton')
        childcare_type_data = data.get('childcare', {}).get('childcare_type')
        
        # Retrieve the corresponding Salary, HousingType, Childcare, and HealthInsurance instances
        try:
            housing_type = HousingType.objects.get(type=housing_type_data, canton__name=canton_data)
            childcare = Childcare.objects.get(childcare_type=childcare_type_data)

            # Calculate the result
            print(f"salary_data={salary_data}, housing_type_value={housing_type.value}, childcare_value={childcare.value}")
            result = salary_data - housing_type.value - childcare.value
        except ObjectDoesNotExist:
            print(f"Failed to retrieve objects with salary_data={salary_data}, housing_type_data={housing_type_data}, canton_data={canton_data}, childcare_type_data={childcare_type_data}")
            return HttpResponse(status=404)

        # Prepare the response dictionary including individual costs
        response_dict = {
            'result': float(result), 
            'housing_cost': float(housing_type.value), 
            'childcare_cost': float(childcare.value)
        }

        # Send the result back to the client
        return JsonResponse(response_dict)

    else:
        return HttpResponse(status=405)


