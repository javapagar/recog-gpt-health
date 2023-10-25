# recog-gpt-health

## Pre-requisites
The project needs:
1. Docker engine install
2. AWS CLI install
3. AWS SAM install
4. API client for test on local like postman (Optional)

## Project structure
This project was create using AWS SAM

```sam init```

### Configuration files
template.yaml file include the necessary configuration for build the AWS Project using the command:

```sam build```

This way, we create the folder .aws-sam with all 
### events folder
It contains event_api_gateway_v2.json file with the event json schema. Before build, we can use this file to testing Lambda Function from a local machine or on AWS platform. For local test we'll use:

```sam local invoke -e ./events/event_api_gateway_v2.json```

### src folder
It contains the python code for lamda function and objects. app.py is the main file.

It's prety important requirements.txt with some libraries to project works.

## Tests
1. With sam you can use:
 * Response ok 200: ```sam local invoke -e ./tests/events/event_api_gateway_v2.json```
 * Response error 400: ```sam local invoke -e ./tests/events/event_400_error.json```
2. You can use an API client, like postman, you need to prepare the body:
```{"symptoms": ["fever", "headache","cough"]}```
Before launch the GET request, We must start API at local with:
```sam local start-api```
you can use the URL: http://127.0.0.1:3000/diagnosis
3. You can run unit test with pytest. Follow next steps:
* Create virtual enviroment ```python3 -m venv venv```
* Activate venv ```source venv/bin/activate``` (linux and mac) or ```venv/Scripts/activate``` for windows OS
* install ./tests/requirements.txt ```pip install -r ./test/requirements.txt```
* Launch tests ```pytest ./tests/unit/ -v```

## Deploy to AWS
1. build ```sam build```
2. Deploy ```sam deploy --guided --profile <profile_name>```