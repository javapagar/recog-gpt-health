from domain.doctor import Doctor
from typing import List

class ChatGPTDoctor(Doctor):
    
    def __init__(self,key_id) -> None:
        self.key_id = key_id
    
    def get_diagnosis(self,symptoms: List[str]) -> str:
        raise NotImplementedError()