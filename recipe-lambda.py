import json

def lambda_handler(event, context):
    #if (event["session"]["application"]["applicationId"] !=
    #        "amzn1.ask.skill.f6d4a4f4-d474-47de-bc4c-d3ad87647de3"):
    #    raise ValueError("Invalid app ID")
    
    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])
    
def on_session_started(session_started_request, session):
    print ("Starting new session.")

def on_launch(launch_request, session):
    return get_welcome_response()

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "ReadRecipes":
        return build_default_recipe()
    elif intent_name == "GetStatus":
        return get_system_status()
    elif intent_name == "GetElevators":
        return get_elevator_status()
    elif intent_name == "GetTrainTimes":
        return get_train_times(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def build_default_recipe():
    session_attributes={}
    return build_response(session_attributes, build_speechlet_response(
        "My Recipes", "You have several recipes that I won't look up now", "", "true"))

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }
