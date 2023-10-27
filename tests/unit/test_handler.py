import json
from http import HTTPStatus
from src import app
from aws_lambda_powertools.utilities.parser import ValidationError

def test_lambda_handler_200(event_v2):

    response = app.lambda_handler(event_v2, "")
    diagnosis_response = json.loads(response["body"])

    assert response["statusCode"] == HTTPStatus.OK
    assert "diagnosis" in response["body"]

def test_lambda_handler_400(event_v2_400_error):  
    response = app.lambda_handler(event_v2_400_error, "")
    assert response['statusCode'] == HTTPStatus.BAD_REQUEST