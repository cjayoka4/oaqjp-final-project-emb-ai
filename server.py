""" Entry point for web server application """
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

"""Return the pathname of the emotion detector root directory."""
@app.route("/emotionDetector")
def emotion_detector():
    """ 
    This function accepts arguments in the form of texts to be analysed
    """
    # Retrieve the text to analyse from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    # Retrieve response text
    response_text = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    return response_text

@app.route("/")
def render_index_page():
    """ This function runs the render template on the HTML template """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)