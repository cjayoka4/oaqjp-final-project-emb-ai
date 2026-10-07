from flask import Flask
from Flask import request, url_for
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotn_detector():
    # Retrieve the text to analyse from the request arguments
    text_to_analyse = request.args.get('textToAnalyse')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    # Parse json response through API
    formatted_response = json.loads(response)
    # Extract emotion dictionary from formatted response
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    # Extract dominant emotion from emotion dictionary
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    # Returning a dictionary containing emotion analysis results
    return "".join("{} : {}\n".format(key, value) for key, value in emotion_dict.items()) + f"dominant_emotion : {dominant_emotion}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
