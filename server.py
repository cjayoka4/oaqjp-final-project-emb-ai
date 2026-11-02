""" Entry point for web server application """
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotn_detector():
    # Retrieve the text to analyse from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    # Parse json response through API
    formatted_response = json.loads(response)
    # Extract emotion dictionary from formatted response and store as emotion_dict
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    # Identifying dominant emotion from extracted emotion dictionary
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    # Merge extracted emotion dictionary and dominant emotion into a new dictionary
    emotion_analysis = {**emotion_dict, 'dominant_emotion': dominant_emotion}
    # Return new dictionary containing emotion analysis results 
    return "\n".join([f"{key} : {value}" for key, value in emotion_analysis.items()])

@app.route("/")
def render_index_page(): # Define route to html template
    return render_template('index.html')

""" Run application on localhost: 5000 """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)