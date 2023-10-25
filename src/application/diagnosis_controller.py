from domain.doctor import Doctor
from domain.symptoms_input import SymptomsInput

class Diagnosiscontroller:
    @staticmethod
    def diagnosis(doctor: Doctor, symptons: SymptomsInput) -> None:
        return doctor.get_diagnosis(symptons.symptoms)