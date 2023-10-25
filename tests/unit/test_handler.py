import json
import pytest
from src import app
from aws_lambda_powertools.utilities.parser import ValidationError

def test_lambda_handler_200(event_v2):

    response = app.lambda_handler(event_v2, "")
    diagnosis_response = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "diagnosis" in response["body"]
    assert diagnosis_response["diagnosis"] == "You might have a common cold. Make sure to rest and stay hydrated."

def test_lambda_handler_400(event_v2_400_error):  
    response = app.lambda_handler(event_v2_400_error, "")
    assert response['statusCode'] == 400