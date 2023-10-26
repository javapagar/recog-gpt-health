from domain.doctor import Doctor
from infrastructure.medical_context import CONTEXT
from typing import List
import os
import openai

class ChatGPTDoctor(Doctor):
    
    def __init__(self) -> None:
        openai.api_key  = os.getenv('OPENAI_API_KEY')
    
    def get_diagnosis(self,symptoms: List[str]) -> str:
        messages = CONTEXT
        symtomps = ",".join(symptoms)
        for_append ={"role":'user','content': f"my symptoms are {symtomps}"}
        messages.append(for_append)

        response = self.__get_completion_from_messages(CONTEXT, temperature=0)
        
        return response
    
    def __get_completion_from_messages(self,messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]