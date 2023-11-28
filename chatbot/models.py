from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory 
from django.conf import settings



# Global variable to store a single conversation memory
global_conversation_memory = ConversationBufferWindowMemory(k=20, memory_key="history")

# Replace with your actual API key
api_key = settings.OPENAI_API_KEY


def reset_conversation_memory():
    global global_conversation_memory
    global_conversation_memory = ConversationBufferWindowMemory(k=20, ai_prefix="AI Assistant", human_prefix="Human")


def chatbot_response(first_message, system_prompt, temperature, message, file=None):


    
    global global_conversation_memory

   

   
    # Determine the appropriate prompt template
    if system_prompt:
        prompt = system_prompt + "\n" + first_message + "\n" """
            Respond in sturctured manner.
            Ask questions one at a time!!

            Current conversation:

            {history}
            Human: {input}
            File: ```{file}```
            AI Assistant:
            """
    else:
        prompt = """
            Act as a helpful assistant.
            If you do not know the answer to a question, truthfully say so.

            Current conversation:
            {history}
            Human: {input}
            File: ```{file}```
            AI Assistant:
            """

    # Initialize the GPT-4 model
    gpt_4 = ChatOpenAI(model_name="gpt-4-1106-preview", openai_api_key=api_key, temperature=temperature, max_tokens=500)

    # Create a prompt template with the necessary input variables
    prompt_template = PromptTemplate(input_variables=["history", "input","file"], template=prompt)

    memory=global_conversation_memory
    # Create a conversation chain with the Langchain components using the shared global conversation memory
    llm_chain = LLMChain(llm=gpt_4, prompt=prompt_template, verbose=False)

    # Generate the reply using the chatbot reply function
    reply = llm_chain.predict(input=message, file=file, history=memory)

    return reply