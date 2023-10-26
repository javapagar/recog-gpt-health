
from domain.doctor import Doctor
from typing import List

class MockDoctor(Doctor):
        
    def get_diagnosis(self,symptoms: List[str]) -> str:
       cold_symptoms_list = ["fever","headache","cough"]
       
       eval_list = [symptom in symptoms for symptom in cold_symptoms_list]
       
       is_cold = eval(" and ".join([str(item) for item in eval_list]))

       if not is_cold:
           return "I'm not sure, it could be a virus"
       
       return "You might have a common cold. Make sure to rest and stay hydrated."
