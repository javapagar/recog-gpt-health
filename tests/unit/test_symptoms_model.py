from src.domain.symptoms_input import SymptomsInputModel, SymptomsInput

def test_symptoms_model(event_v2):
    symptoms_body = SymptomsInputModel.model_validate(event_v2)
        
    symptoms_input = symptoms_body.body

    assert symptoms_input.symptoms[0] == "fever"