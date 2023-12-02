from django.views import View
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

import PyPDF2
import io

from .models import chatbot_response,history_init, reset_conversation_memory  # Ensure correct import path


def read_pdf(uploaded_file):
    # Read the file as a byte stream
    file_stream = io.BytesIO(uploaded_file.read())
    pdf_reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() if page.extract_text() else ""
    return text

marker = False

@method_decorator(csrf_exempt, name='dispatch')
class ChatbotView(View):
    def post(self, request, *args, **kwargs):

        global marker

        try:
            print("Received request")

           

            # Decode the JSON request body
            # For multipart/form-data, the JSON data is in 'message' field
            if request.content_type == 'multipart/form-data':
                data = json.loads(request.POST.get('message'))
            else:
                data = json.loads(request.body.decode('utf-8'))

            # Check if the reset key is present and True
            if data.get("reset") == True:
                reset_conversation_memory()
                return JsonResponse({"message": "Conversation memory reset."}, status=200)

            # Process regular chatbot messages
            system_message = data.get("systemMessage", "")
            user_message = data.get("message", "")
            first_message = data.get("firstMessage", "")
            print("First message: ",first_message)

            if first_message and marker == False:

                history_init(first_message)
                
                marker = True

            
            
            file = request.FILES.get('file')

            if file:
                
                print("File received")
            else:
                print("No file received")

            file_text = read_pdf(file) if file else "No file attached"                
            

            # Generate the response from the chatbot
            response_data = chatbot_response(system_message, 1, user_message, file_text)  # This should return a string

            # Format the response by replacing newlines with HTML line breaks
            # and wrap the response in a div with the chatbot-message class
            formatted_response = "<div class='chatbot-message'>{}</div>".format(
                response_data.replace("\n", "<br />")
            )

            # Send the HTML formatted response
            return HttpResponse(formatted_response, content_type="text/html")

        except Exception as e:
            # Handle errors
            return HttpResponse(f"Error: {str(e)}", status=400, content_type="text/html")
