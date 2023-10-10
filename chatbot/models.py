from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain.chains import SequentialChain, LLMChain 


from django.conf import settings


api_key = settings.OPENAI_API_KEY


chat_model = ChatOpenAI(openai_api_key=api_key,
                        temperature=1,
                        max_tokens=500,
                        model_name="gpt-3.5-turbo")



def clean_response(response):
    # Assuming `response` has a `.content` attribute that's a string
    response_content = response.content
    
    # Remove "AI:" and "Human message:" from the response
    cleaned_content = response_content.replace("AI:", "").replace("Human message:", "").strip()
    
    # Update the content of the response object
    response.content = cleaned_content
    
    return response

def get_response(query):
    human_message = HumanMessage(content=query)
    response = chat_model([human_message])

    response = clean_response(response)
    lower_content = response.content.lower()

    if "openai" in lower_content or "gpt" in lower_content:
        return "I'm sorry, I can only provide information related to Switzerland. Please ask a relevant question."
    
    if len(response.content.split()) > 200:
        template1 = "Condense this in 200 tokens\n{response}"
        prompt1 = ChatPromptTemplate.from_template(template1)
        chain1 = LLMChain(llm=chat_model, prompt=prompt1, output_key="condense_message")
        seq_chain = SequentialChain(chains=[chain1],
                                    input_variables=["response"],
                                    output_variables=["condense_message"],
                                    verbose=True)
        content = seq_chain(response.content)
        return content
    else:
        return response.content
