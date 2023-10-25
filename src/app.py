from domain.symptoms_input import SymptomsInputModel, SymptomsInput
from aws_lambda_powertools.utilities.parser import parse, ValidationError
from aws_lambda_powertools.utilities.typing import LambdaContext
from infrastructure.mock_doctor import MockDoctor
from application.diagnosis_controller import Diagnosiscontroller
import json

def get_json_response(status_code: int, json_resp:json)-> dict:
    return {
            "statusCode": status_code,
            "body": json_resp,
            'headers': {
                'Content-Type': 'application/json',
            },
        }

def lambda_handler(event:SymptomsInputModel, context:LambdaContext):
    try:
        symptoms_body: SymptomsInputModel = parse(event = event,model=SymptomsInputModel)
        
        symptoms_input: SymptomsInput = symptoms_body.body
        doctor = MockDoctor()

        diagnosis = Diagnosiscontroller.diagnosis(doctor,symptoms_input)
        
        json_diagnosis = json.dumps({"diagnosis": diagnosis})
        
        return get_json_response(200,json_diagnosis)
        
    except ValidationError as e:
        json_error = json.dumps({"message": "Symptoms bad request error"})
        return get_json_response(400,json_error)
    
    except Exception as e:
        json_error = json.dumps({"message": "Server Error"})
        return get_json_response(500,json_error)
