import requests # Import the requests library to handle HTTP requests
import json

# Define emotion detection function 
def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analysed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion and scores dictionary from formatted response
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting dominant emotion from emotion dictionary (USE OR REMOVE - CHECK RETURN STATEMENT)
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
	
    # Returning a dictionary containing emotion analysis results
    return "".join("{} : {}\n".format(key, value) for key, value in emotion_dict.items()) + f"dominant_emotion : {dominant_emotion}"
