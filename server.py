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
    # Extract emotion dictionary from formatted response
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    # Extract dominant emotion from emotion dictionary
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    # Check if the dominant emotion is None, indicating an error or invalid text input
    if dominant_emotion == None:
      return "Invalid text! Please try again!"
    else:
    # Merge extracted emotion dictionary and dominant emotion into a new dictionary
    emotion_analysis = {**emotion_dict, 'dominant_emotion': dominant_emotion}
    # Return formatted dictionary containing emotion analysis results 
    return "\n".join([f"{key} : {value}" for key, value in emotion_analysis.items()

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)