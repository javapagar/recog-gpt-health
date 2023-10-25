from domain.symptoms_input import SymptomsInputModel
from aws_lambda_powertools.utilities.parser import parse, ValidationError
from aws_lambda_powertools.utilities.typing import LambdaContext

import json

def lambda_handler(event:SymptomsInputModel, context:LambdaContext):
    try:
        symptoms_body: SymptomsInputModel = parse(event = event,model=SymptomsInputModel)
    
        return {
            "statusCode": 200,
            "body": json.dumps({
                "diagnosis": "You might have a common cold. Make sure to rest and stay hydrated."}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
    except ValidationError as e:
        print(e)
        return {
        'statusCode': '400',
        'body': json.dumps({"message": "Symptoms bad request error"}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    except Exception as e:
        print(e)
        return {
        'statusCode': '500',
        'body': json.dumps({"message": "Server Error"}),
        'headers': {
            'Content-Type': 'application/json',
        },
        }
