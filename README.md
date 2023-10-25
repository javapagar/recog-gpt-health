# recog-gpt-health

## Pre-requisites
The project needs:
1. Docker engine install
2. AWS CLI install
3. AWS SAM install

## Project structure
This project was create using AWS SAM

### Configuration files
template.yaml file include the necessary configuration for build the AWS Project using the command:

```sam build```


### events folder
It contains event_api_gateway_v2.json file with the event json schema. we can use this file to testing Lambda Function from a local machine:

```sam invoke -e ./events/event_api_gateway_v2.json```

### src folder
It contains the python code for lamda function and objects. app.py is the main file.

It's prety important requirements.txt with some libraries to project works.