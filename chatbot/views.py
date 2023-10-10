import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import get_response  # Ensure correct import path



@method_decorator(csrf_exempt, name='dispatch')
class ChatbotView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            print("Received data:", data)
            formatted_string = "System message: Content = You are the SwissCost chatbot, specialized in providing short answers to questions about expenses in various cantons of Switzerland. You kindly decline to respond to any inquiries that are not related to Switzerland or its expenses."


            for i in range(len(data['conversations'])):
                speaker = data['conversations'][i]['speaker']
                text = data['conversations'][i]['text']
                formatted_string += f"   {speaker}{text}"
            print(formatted_string)  # This should print 
            query = formatted_string 
            # Get the conversation history

            # Generate response using the model
            chatbot_response = get_response(query)
            
            # Add the chatbot's response to the history
            
            response_data = {"AI": chatbot_response}
            
            return JsonResponse(response_data)
        except Exception as e:
            print("Error:", e)  # Print the error for debugging
            return JsonResponse({"error": str(e)}, status=400)