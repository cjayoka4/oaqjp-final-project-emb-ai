import requests # Import the requests library to handle HTTP requests
import json

# Define emotion detection function 
def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the payload with the text to be analysed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    status_code = response.status_code
   
    if status_code == 400:
        formatted_response = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None } 

    elif status_code == 200:
        # Parse the JSON response from the API
        formatted_response = json.loads(response.text)
        # Extract emotion dictionary from formatted response and store as emotion_dict
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        # Identifying dominant emotion
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        # Merge extracted emotion dictionary and dominant emotion into a new dictionary
        emotion_analysis = {**emotion_dict, 'dominant_emotion': dominant_emotion}
        # Return formatted dictionary containing emotion analysis results 
        return emotion_analysis
    
    # For any other unexpected status codes, set emotion and score to None
    else:
        formatted_response = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }