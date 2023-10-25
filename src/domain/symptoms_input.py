from aws_lambda_powertools.utilities.parser import BaseModel, validator
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventV2Model
from typing import List
import json

class SymptomsInput(BaseModel):
    symptoms: List[str]

class SymptomsInputModel(APIGatewayProxyEventV2Model):
    body: SymptomsInput

    @validator("body",pre= True)
    def body_to_dict(cls, value: str):
        return json.loads(value)