from abc import ABC,abstractmethod
from typing import List

class Doctor(ABC):
    @abstractmethod
    def get_diagnosis(self,symptons: List[str])-> str:
        ...