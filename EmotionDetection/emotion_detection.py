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
       
    # If the response status code is 200, extract the emotion and score from the response
    if response.status_code == 200:
        # Parse the JSON response from the API
	    formatted_response = json.loads(response.text)
        # Extract emotion dictionary from formatted response and store as emotion_dict
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        # Identifying dominant emotion from extracted emotion dictionary
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        # Merge extracted emotion dictionary and dominant emotion into a new dictionary
        emotion_analysis = {**emotion_dict, 'dominant_emotion': dominant_emotion}
    
    # If the response status code is 400, extract dictionary with key values set to None
    elif response.status_code == 400:
        # Parse the JSON response from the API
	    formatted_response = json.loads(response.text)
        # Parse formatted response as a new dictionary
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
	    # Set dictionary values for each emotion to NONE
        emotion_dict = {key: None for key in emotion_dict}
        # Return None for emotions
        return "\n".join([f"{key} : {value}" for key, value in emotion_dict.items()])

    # For any other unexpected status codes, set both emotion and score to None
    else:
	    # Parse the JSON response from the API
	    formatted_response = json.loads(response.text)
        # Parse formatted response as a new dictionary
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
	    # Set dictionary values for each emotion to NONE
        emotion_dict = {key: None for key in emotion_dict}
        # Return None for emotions
        return "\n".join([f"{key} : {value}" for key, value in emotion_dict.items()])
  
    # Return formatted dictionary containing emotion analysis results 
    return "\n".join([f"{key} : {value}" for key, value in emotion_analysis.items()])